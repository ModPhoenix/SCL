"""scl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from django.contrib.flatpages.views import flatpage

from blog.models import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    url(r'^', include('blog.urls', namespace='blog')),
    url(r'^guides/', include('guides.urls', namespace='guides')),
    url(r'^comments/', include('comments.urls', namespace='comments')),
    url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('profiles.urls', namespace='profiles')),
    # url(r'^db/', include('database.urls', namespace='database')),
    url(r'^', include('attachments.urls', namespace='attachments')),
    url(r'^admin/', admin.site.urls),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap'),
    url(r'^about/$', flatpage, {'url': '/about/'}, name='about'),
    url(r'^careers/$', flatpage, {'url': '/careers/'}, name='careers'),
    url(r'^terms/$', flatpage, {'url': '/terms/'}, name='terms'),
    url(r'^privacy/$', flatpage, {'url': '/privacy/'}, name='privacy'),
    url(r'^tellme/', include("tellme.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)