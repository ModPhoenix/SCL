from django.shortcuts import render, get_object_or_404

from .models import User

def user_profile(request, username):
    user_prolile = get_object_or_404(User, username=username)
    context = {'user_prolile': user_prolile}
    return render(request, 'profiles/profiles.html', context)
