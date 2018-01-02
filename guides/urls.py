from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.GuideListView.as_view(), name='index'),
    url(r'^page/(?P<page>\d+)/$', views.GuideListView.as_view(), name='index_pagination'),
    url(r'^(?P<id>\d+)-(?P<slug>[\w-]+)/$', views.GuideDetailView.as_view(), name='guide_detail'),
    url(r'^create-guide/$', views.GuideCreateView.as_view(), name='create_guide'),
    url(r'^(?P<id>\d+)-(?P<slug>[\w-]+)/edit/$', views.GuideUpdateView.as_view(), name='edit_guide'),
]
