import json

from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import User
from blog.models import Post
from comments.models import Comment
from .forms import PublicProfileForm
from allauth.account.views import PasswordChangeView, EmailView


def user_profile(request, username):
    user_prolile = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user_prolile).select_related()
    comments = Comment.objects.filter(user=user_prolile)
    count_comments = comments.count()
    count_posts = posts.count()
    context = {
        'user_prolile': user_prolile,
        'posts': posts,
        'count_posts': count_posts,
        'count_comments': count_comments,
    }
    return render(request, 'profiles/profiles.html', context)

def settings_profile(request):

    user = request.user

    if request.method == "POST":
        form = PublicProfileForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            #user.birthdate = form.cleaned_data['birthdate']
            user.biography = form.cleaned_data['biography']
            user.location = form.cleaned_data['location']
            user.organization = form.cleaned_data['organization']
            user.handle = form.cleaned_data['handle']
            user.save()

    else:
        form = PublicProfileForm(instance=user)
    
    return render(request, 'profiles/settings_profile.html', {'form': form})

def avatar_upload(request):
    if request.FILES:
        the_file = request.FILES['image']
        allowed_types = ['image/jpeg', 'image/jpg', 'image/pjpeg', 'image/x-png', 'image/png', 'image/gif']
        if not the_file.content_type in allowed_types:
            return HttpResponse(json.dumps({'error': _('You can only upload images.')}),
                                content_type="application/json")
        # Other data on the request.FILES dictionary:
        # filesize = len(file['content'])
        # filetype = file['content-type']
        user = request.user
        user.avatar = the_file
        user.save()

        link = user.avatar.url

        # return JsonResponse({'link': link})
        return HttpResponse(json.dumps({'link': link, 'name': "name",}), content_type="application/json")

class SettingsPasswordChangeView(PasswordChangeView):
    template_name = (
        "profiles/settings_password_change.html")
    success_url = reverse_lazy("profiles:settings_password_change")

settings_password_change = login_required(SettingsPasswordChangeView.as_view())

class SettingsEmailView(EmailView):
    template_name = (
        "profiles/settings_email.html")
    success_url = reverse_lazy("profiles:settings_email")

settings_email = login_required(SettingsEmailView.as_view())