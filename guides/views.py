from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator

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
    context_object_name = 'guide'
    template_name = 'guides/guide_detail.html'


@method_decorator(login_required, name='dispatch')
class GuideCreateView(CreateView):
    model = Guide
    fields = ['title', 'content', 'published']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.request.user.is_staff:
            form.instance.moderation = True
        else:
            form.instance.moderation = False
        return super(GuideCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.user.is_staff:
            messages.info(
                self.request, 'Гайд успешно опубликован.')
            return self.object.get_absolute_url()
        else:
            messages.info(
                self.request, 'Гайд успешно добавлен и был отправлен на модерацию.')

            return reverse("blog:index")


@method_decorator(login_required, name='dispatch')
class GuideUpdateView(UpdateView):
    model = Guide
    fields = ['title', 'content', 'published']
    template_name = 'blog/post_create.html'

