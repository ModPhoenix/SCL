from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^users/(?P<username>\w+)$', views.user_profile, name='user_profile'),
]
