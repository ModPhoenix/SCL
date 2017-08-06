from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from editor.utils import screening

from .models import Post
from .forms import PostForm


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def detail(request, id, slug):
    post = get_object_or_404(Post, slug=slug, id=id)
    context = {'post': post}
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
