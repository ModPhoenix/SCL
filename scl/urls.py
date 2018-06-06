from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from django.contrib.sitemaps import views

from django.contrib.flatpages.views import flatpage

from .views import TaggedList, TagAutocomplete

from .sitemaps import PostSitemap, GuideSitemap, StaticViewSitemap

from scl.feed import LatestPostsFeed, LatestGuidesFeed

sitemaps = {
    'posts': PostSitemap,
    'guides': GuideSitemap,
    'pages': StaticViewSitemap,
}

urlpatterns = [
    url(r'^favicon.ico$',RedirectView.as_view(url=staticfiles_storage.url('img/favicon/favicon.ico')),name="favicon"),
    url(r'^', include('blog.urls', namespace='blog')),
    url(r'^guides/', include('guides.urls', namespace='guides')),
    url(r'^comments/', include('comments.urls', namespace='comments')),
    url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('profiles.urls', namespace='profiles')),
    url(r'^db/', include('knowledgebase.urls', namespace='knowledgebase')),
    url(r'^', include('attachments.urls', namespace='attachments')),
    url(r'^tag/(?P<slug>[\w-]+)/$', TaggedList.as_view(), name='tagged'),
    url(r'^tag/(?P<slug>[\w-]+)/page/(?P<page>\d+)/$', TaggedList.as_view(), name='tagged_pagination'),
    url(r'^admin/', admin.site.urls),

    url(r'^tag-autocomplete/$',TagAutocomplete.as_view(),name='tag-autocomplete',),

    url(r'^about/$', flatpage, {'url': '/about/'}, name='about'),
    url(r'^careers/$', flatpage, {'url': '/careers/'}, name='careers'),
    url(r'^terms/$', flatpage, {'url': '/terms/'}, name='terms'),
    url(r'^privacy/$', flatpage, {'url': '/privacy/'}, name='privacy'),

    url(r'^sitemap\.xml$', views.index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', views.sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    
    url(r'^feed/posts/$', LatestPostsFeed()),
    url(r'^feed/guides/$', LatestGuidesFeed()),

    url(r'^tellme/', include("tellme.urls")),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)