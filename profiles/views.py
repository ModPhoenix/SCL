import json

from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import to_locale, get_language, ugettext_lazy as _

from .models import User
from blog.models import Post
from comments.models import Comment
from guides.models import Guide
from .forms import PublicProfileForm
from allauth.account.views import PasswordChangeView, EmailView


class UserProfile(ListView):
    paginate_by = 20
    template_name = 'profiles/profiles.html'

    def get_queryset(self):
        self.user_prolile = get_object_or_404(User, username=self.kwargs['username'])
        return Post.objects.filter(author=self.user_prolile, published=True, moderation=True).select_related()


    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        
        context['user_prolile'] = self.user_prolile
        context['count_posts'] = self.object_list.count()
        context['count_posts_drafts'] = Post.objects.filter(author=self.user_prolile, published=False, moderation=True).count()
        context['count_comments'] = Comment.objects.filter(user=self.user_prolile).count()
        context['count_guides'] = Guide.objects.filter(author=self.user_prolile, published=True, moderation=True).count()
        context['count_guides_drafts'] = Guide.objects.filter(author=self.user_prolile, published=False, moderation=True).count()
        return context


@method_decorator(login_required, name='dispatch')
class UserProfileDrafts(ListView):
    paginate_by = 20
    template_name = 'profiles/profiles.html'

    def get_queryset(self):
        self.user_prolile = get_object_or_404(User, username=self.kwargs['username'])
        return Post.objects.filter(author=self.user_prolile, published=False, moderation=True).select_related()


    def get_context_data(self, **kwargs):
        context = super(UserProfileDrafts, self).get_context_data(**kwargs)
        
        context['user_prolile'] = self.user_prolile
        context['count_posts'] = Post.objects.filter(author=self.user_prolile, published=True, moderation=True).count()
        context['count_posts_drafts'] = self.object_list.count()
        context['count_comments'] = Comment.objects.filter(user=self.user_prolile).count()
        context['count_guides'] = Guide.objects.filter(author=self.user_prolile, published=True, moderation=True).count()
        context['count_guides_drafts'] = Guide.objects.filter(author=self.user_prolile, published=False, moderation=True).count()
        return context


class UserProfileGuides(ListView):
    paginate_by = 20
    template_name = 'profiles/profiles.html'

    def get_queryset(self):
        self.user_prolile = get_object_or_404(User, username=self.kwargs['username'])
        return Guide.objects.filter(author=self.user_prolile, published=True, moderation=True).select_related()


    def get_context_data(self, **kwargs):
        context = super(UserProfileGuides, self).get_context_data(**kwargs)
        
        context['user_prolile'] = self.user_prolile
        context['count_posts'] = Post.objects.filter(author=self.user_prolile, published=True, moderation=True).count()
        context['count_posts_drafts'] = Post.objects.filter(author=self.user_prolile, published=False, moderation=True).count()
        context['count_comments'] = Comment.objects.filter(user=self.user_prolile).count()
        context['count_guides'] = self.object_list.count()
        context['count_guides_drafts'] = Guide.objects.filter(author=self.user_prolile, published=False, moderation=True).count()
        return context


@method_decorator(login_required, name='dispatch')
class UserProfileGuidesDrafts(ListView):
    paginate_by = 20
    template_name = 'profiles/profiles.html'

    def get_queryset(self):
        self.user_prolile = get_object_or_404(User, username=self.kwargs['username'])
        return Guide.objects.filter(author=self.user_prolile, published=False, moderation=True).select_related()


    def get_context_data(self, **kwargs):
        context = super(UserProfileGuidesDrafts, self).get_context_data(**kwargs)
        
        context['user_prolile'] = self.user_prolile
        context['count_posts'] = Post.objects.filter(author=self.user_prolile, published=True, moderation=True).count()
        context['count_posts_drafts'] = Post.objects.filter(author=self.user_prolile, published=False, moderation=True).count()
        context['count_comments'] = Comment.objects.filter(user=self.user_prolile).count()
        context['count_guides'] = Guide.objects.filter(author=self.user_prolile, published=True, moderation=True).count()
        context['count_guides_drafts'] = self.object_list.count()
        return context


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
        user_prof = request.user
        user_prof.avatar = the_file
        user_prof.save()

        link = user_prof.avatar.url

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