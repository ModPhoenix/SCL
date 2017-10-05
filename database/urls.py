from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.db_index, name='db_index'),
    url(r'^ships/(?P<slug>[\w-]+)/$', views.ship_detail, name='ship_detail'),
]
