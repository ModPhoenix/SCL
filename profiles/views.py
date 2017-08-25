from django.shortcuts import render, get_object_or_404

from .models import User
from blog.models import Post

def user_profile(request, username):
    user_prolile = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user_prolile)
    context = {
        'user_prolile': user_prolile,
        'posts': posts,
    }
    return render(request, 'profiles/profiles.html', context)
