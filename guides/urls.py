from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)-(?P<slug>[\w-]+)$', views.guide_detail, name='guide_detail'),
    url(r'^create-post$', views.create_guide, name='create_guide'),
    url(r'^(?P<id>\d+)-(?P<slug>[\w-]+)/edit$', views.edit_guide, name='edit_guide'),
]
