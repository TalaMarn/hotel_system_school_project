from django.shortcuts import render, redirect
from .models import Room
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('staff_dashboard')
            return redirect('customer_dashboard')
        messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'That username is already taken.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'An account with that email already exists.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            if role == 'staff':
                user.is_staff = True
                user.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')

    return render(request, 'register.html')

def roomList(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }
    return render(request, 'room_list.html', context)