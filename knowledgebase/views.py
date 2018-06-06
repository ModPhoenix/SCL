from django.shortcuts import render, get_object_or_404

from .models import (
    Page,
    Ship,
    Company,
)


def db_index(request):
    ships = Ship.objects.all()[:5]
    pages = Page.objects.all()

    context = {
        'ships': ships,
        'pages': pages,
    }

    return render(request, 'knowledgebase/db_index.html', context)


def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, published=True)

    context = {
        'page': page,
    }

    return render(request, 'knowledgebase/db_page.html', context)


def page_edit(request, slug):
    pass


def ships_category(request):
    ships = Ship.objects.all().select_related('manufacturer')

    context = {
        'ships': ships,
        }

    return render(request, 'knowledgebase/db_category.html', context)


def ship_detail(request, slug):
    ship = get_object_or_404(Ship, slug=slug)

    context = {
        'ship': ship,
    }

    return render(request, 'knowledgebase/ship_detail.html', context)
