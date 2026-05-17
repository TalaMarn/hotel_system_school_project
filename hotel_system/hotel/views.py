from django.shortcuts import render
from .models import Room
from django.contrib.auth.decorators import login_required

# Create your views here.

# Welcome View
def hotel_welcome(request):
    rooms = Room.objects.all().order_by('id')[:3]
    context = {
        'rooms': rooms,
    }

    return render(request, 'hotel_welcome.html', context)

@login_required
def customer_dashboard(request):
    rooms = Room.objects.all().order_by('id')[:3]
    context = {
        'rooms': rooms,
    }

    return render(request, 'customer_dashboard.html', context)

@login_required
def staff_dashboard(request):
    rooms = Room.objects.all().order_by('id')[:3]
    context = {
        'rooms': rooms,
    }

    return render(request, 'staff_dashboard.html', context)

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def roomList(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }
    return render(request, 'room_list.html', context)