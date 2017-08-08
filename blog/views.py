from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from editor.utils import screening

from .models import Post
from comments.models import Comment
from .forms import PostForm
from comments.forms import CommentForm


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def post_detail(request, id, slug):
    post = get_object_or_404(Post, slug=slug, id=id)

    comments = Comment.objects.filter_by_instance(post).select_related()

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
        parent_obj = None
        new_comment = Comment.objects.create(
            author=request.user,
            content_type=content_type,
            object_id=object_id,
            content=content_data,
            parent=parent_obj,
        )

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'blog/post_detail.html', context)


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.content = screening(form.cleaned_data['content'])
            print(post.content)
            post.save()
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})


def edit(request, id, slug):
    post = get_object_or_404(Post, slug=slug, id=id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.content = screening(form.cleaned_data['content'])
            post.save()
            return redirect(post.get_absolute_url())
    else:
        print(2)
        form = PostForm(instance=post)
        print(form)

    return render(request, 'blog/post_create.html', {'form': form})
