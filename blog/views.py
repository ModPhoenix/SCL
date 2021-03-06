from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from editor.utils import screening
from django.urls import reverse
import reversion

from .models import Post
from .forms import PostForm


class PostList(ListView):
    context_object_name = 'posts'
    paginate_by = 10
    queryset = Post.objects.filter(
        published=True, moderation=True).select_related()
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)

        context['tags'] = Post.tags.most_common()[:10]
        return context


def post_detail(request, id, slug):
    post = get_object_or_404(
        Post.objects.select_related(), slug=slug, id=id, moderation=True)

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

                if request.user.is_staff:
                    post.moderation = True
                else:
                    post.moderation = False

                post.save()

                reversion.set_user(request.user)
                reversion.set_comment(
                    "Пост создан, пользователем: %s" % request.user.username)

                if request.user.is_staff:
                    messages.info(
                        request, 'Пост успешно опубликован.')
                    return redirect(post.get_absolute_url())
                else:
                    messages.info(
                        request, 'Пост успешно добавлен и был отправлен на модерацию.')
                    return redirect(reverse("blog:index"))
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
