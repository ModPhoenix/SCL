from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from editor.utils import screening
import reversion

from .models import Post
from database.models import Funding
from .forms import PostForm
from attachments.models import Attachment


class PostList(ListView):
    context_object_name = 'posts'
    paginate_by = 10
    queryset = Post.objects.all().select_related()
    template_name = 'home.html'


def post_detail(request, id, slug):
    post = get_object_or_404(Post.objects.select_related(), slug=slug, id=id)

    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            with reversion.create_revision():
                post = form.save(commit=False)
                post.author = request.user
                post.content = screening(form.cleaned_data['content'])
                post.save()

                reversion.set_user(request.user)
                reversion.set_comment(
                    "Пост создан, пользователем: %s" % request.user.username)

                return redirect(post.get_absolute_url())
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

@login_required
def edit(request, id, slug):
    post = get_object_or_404(Post, slug=slug, id=id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            with reversion.create_revision():
                post = form.save(commit=False)
                post.author = request.user
                post.content = screening(form.cleaned_data['content'])
                post.updated_at = timezone.now()
                post.save()

                reversion.set_user(request.user)
                reversion.set_comment(
                    "Пост отредактирован на сайте, пользователем: %s" % request.user.username)

                return redirect(post.get_absolute_url())
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_create.html', {'form': form})
