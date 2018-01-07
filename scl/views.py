from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404

from dal import autocomplete

from taggit.models import Tag, TaggedItem

class TaggedList(ListView):
    context_object_name = 'tagged_list'
    paginate_by = 20
    template_name = 'tags/tag_item_list.html'

    def get_queryset(self):
        return TaggedItem.objects.filter(tag__slug=self.kwargs['slug']).prefetch_related('content_object', 'content_object__author').order_by('id').reverse()

    def get_context_data(self, **kwargs):
        context = super(TaggedList, self).get_context_data(**kwargs)

        try:
            tag = Tag.objects.get(slug=self.kwargs['slug'])
        except Tag.DoesNotExist:
            raise Http404("Тег не найден.")
        
        context['tag'] = tag
        return context


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Tag.objects.none()

        qs = Tag.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs