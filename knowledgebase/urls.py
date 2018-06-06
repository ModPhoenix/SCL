from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.db_index, name='index'),
    url(r'^ships/$', views.ships_category, name='ships_category'),
    url(r'^(?P<slug>[\w-]+)/$', views.page_detail, name='page_detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.page_edit, name='page_edit'),
    url(r'^ships/(?P<slug>[\w-]+)/$', views.ship_detail, name='ship_detail'),
]
