from django.shortcuts import render, get_object_or_404

from .models import Ship, Company

def db_index(request):
    ships = Ship.objects.all()

    context = {
        'ships': ships,
        }

    return render(request, 'database/db_index.html', context)

def ship_detail(request, slug):
    ship = get_object_or_404(Ship, slug=slug)

    context = {
        'ship': ship,
    }

    return render(request, 'database/ship_detail.html', context)
