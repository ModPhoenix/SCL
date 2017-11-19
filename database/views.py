from django.shortcuts import render, get_object_or_404

from .models import (
    Category,
    Ship,
    Company,
)

def db_index(request):
    ships = Ship.objects.all()[:5]

    context = {
        'ships': ships,
    }

    return render(request, 'database/db_index.html', context)

def ships_category(request):
    ships = Ship.objects.all().select_related('manufacturer')

    context = {
        'ships': ships,
        }

    return render(request, 'database/db_category.html', context)

def ship_detail(request, slug):
    ship = get_object_or_404(Ship, slug=slug)

    context = {
        'ship': ship,
    }

    return render(request, 'database/ship_detail.html', context)
