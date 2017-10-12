from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^users/(?P<username>\w+)$', views.user_profile, name='user_profile'),
    url(r'^settings/profile/$', views.settings_profile, name='settings_profile'),
    url(r'^settings/profile/upload/$', views.avatar_upload, name='avatar_upload'),
]
