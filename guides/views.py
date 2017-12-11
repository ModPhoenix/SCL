from django.shortcuts import render

from .models import Guide

def index(request):
    guides = Guide.objects.all().select_related()

    context = {
        'guides': guides,
    }

    return render(request, 'guides/guides_index.html', context)

def guide_detail(request):
    pass

def create_guide(request):
    pass

def edit_guide(request):
    pass