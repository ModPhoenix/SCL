from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.PostList.as_view(), name='index'),
    url(r'^(?P<id>\d+)-(?P<slug>[\w-]+)$', views.post_detail, name='detail'),
    url(r'^create-post$', views.create_post, name='create_post'),
    url(r'^(?P<id>\d+)-(?P<slug>[\w-]+)/edit$', views.edit, name='edit_post'),
]
