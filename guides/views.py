from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404

from .models import Guide

class GuideListView(ListView):
    context_object_name = 'guides'
    queryset = Guide.objects.all().select_related()
    template_name = 'guides/guides_index.html'

class GuideDetailView(DetailView):
    model = Guide
    context_object_name = 'guide'
    pk_url_kwarg = 'pk'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True
    template_name = 'guides/guide_detail.html'


class GuideCreateView(CreateView):
    model = Guide
    fields = ['title', 'content', 'published']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(GuideCreateView, self).form_valid(form)

def create_guide(request):
    pass

def edit_guide(request):
    pass