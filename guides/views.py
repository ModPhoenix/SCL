from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

from .models import Guide


class GuideListView(ListView):
    context_object_name = 'guides'
    paginate_by = 10
    queryset = Guide.objects.filter(published=True, moderation=True).select_related()
    template_name = 'guides/guides_index.html'


class GuideDetailView(DetailView):
    model = Guide
    context_object_name = 'guide'
    pk_url_kwarg = 'id'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True
    template_name = 'guides/guide_detail.html'


@method_decorator(login_required, name='dispatch')
class GuideCreateView(CreateView):
    model = Guide
    fields = ['title', 'content', 'published']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(GuideCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class GuideUpdateView(UpdateView):
    model = Guide
    fields = ['title', 'content', 'published']
    template_name = 'blog/post_create.html'


def create_guide(request):
    pass


def edit_guide(request):
    pass
