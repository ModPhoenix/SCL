from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^users/(?P<username>\w+)/$', views.UserProfile.as_view(), name='user_profile'),
    url(r'^users/(?P<username>\w+)/page/(?P<page>\d+)/$', views.UserProfile.as_view(), name='user_profile_pagination'),
    url(r'^users/(?P<username>\w+)/drafts/$', views.UserProfileDrafts.as_view(), name='user_profile_drafts'),
    url(r'^users/(?P<username>\w+)/guides/$', views.UserProfileGuides.as_view(), name='user_profile_guides'),
    url(r'^users/(?P<username>\w+)/guides/drafts/$', views.UserProfileGuidesDrafts.as_view(), name='user_profile_guides_drafts'),
    url(r'^settings/profile/$', views.settings_profile, name='settings_profile'),
    url(r'^settings/profile/upload/$', views.avatar_upload, name='avatar_upload'),
    url(r'^settings/account/$', views.settings_password_change, name='settings_password_change'),
    url(r'^settings/email/$', views.settings_email, name='settings_email'),
]
