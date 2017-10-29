from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from editor.utils import screening
import reversion

from .models import Post
from comments.models import Comment
from database.models import Funding
from .forms import PostForm
from comments.forms import CommentForm
from attachments.models import Attachment


def index(request):
    posts = Post.objects.all().select_related()
    #funding = Funding.objects.all()[:1]
    funding = Funding.objects.latest('date')

    context = {
        'posts': posts,
        'funding': funding,
    }
    return render(request, 'blog/home.html', context)


def post_detail(request, id, slug):
    post = get_object_or_404(Post.objects.select_related(), slug=slug, id=id)

    comments = Comment.objects.filter_by_instance(post).select_related()

    comments_parent = []
    comments_children = []

    for comment in comments:

        if comment.parent_id is None:
            comments_parent.append(comment)
        else:
            comments_children.append(comment)

    initial_data = {
        'content_type': post.get_conttent_type,
        'object_id': post.id,
    }
    comment_form = CommentForm(request.POST or None, initial=initial_data)
    if comment_form.is_valid():
        c_type = comment_form.cleaned_data['content_type']
        content_type = ContentType.objects.get(model=c_type)
        object_id = comment_form.cleaned_data['object_id']
        content_data = comment_form.cleaned_data['content']
        parent_object = None

        try:
            parent_id = comment_form.cleaned_data['parent_id']
        except:
            parent_id = None

        if parent_id != None:
            print("parent_id != None")
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists():
                parent_object = parent_qs.first()

        new_comment = Comment.objects.create(
            author=request.user,
            content_type=content_type,
            object_id=object_id,
            content=content_data,
            parent=parent_object,
        )
        return HttpResponseRedirect("%s#comment-%s" % (new_comment.content_object.get_absolute_url(), new_comment.id))

    context = {
        'post': post,
        'comments_parent': comments_parent,
        'comments_children': comments_children,
        'comment_form': comment_form,
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
                    "Пост создан на сайте, пользователем: %s" % request.user.username)

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
