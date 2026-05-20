from django.shortcuts import render, redirect, get_object_or_404
from .models import Room
from .forms import LoginForm, BookingForm , RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# Welcome View


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
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user:
                login(request, user)
                if user.is_staff:
                    return redirect('staff_dashboard')
                return redirect('customer_dashboard')
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {'form': form})

def register_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            role = form.cleaned_data['role']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is already taken.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'An account with that email already exists.')
            elif password != confirm_password:
                messages.error(request, 'Passwords do not match.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                if role == 'Staff':
                    user.is_staff = True
                    user.save()
                messages.success(request, 'Account created successfully. Please log in.')
                return redirect('login')

    return render(request, 'register.html', {'form': form})



@login_required
def roomList(request):
    rooms = Room.objects.filter(isAvailable=True)
    context = {
        'rooms': rooms,
    }
    return render(request, 'room_list.html', context)

def booking_view(request, room_id):

    room = get_object_or_404(Room, id=room_id)

    # Prevent booking unavailable room
    if not room.isAvailable:
        return render(request, '404.html')

    if request.method == 'POST':

        form = BookingForm(request.POST, request.FILES)

        if form.is_valid():

            booking = form.save(commit=False)

            # connect selected room
            booking.room = room

            # save booking
            booking.save()

            # update room status
            room.isAvailable = False
            room.save()

            return redirect('success')

    else:
        form = BookingForm()

    return render(request, 'booking_page.html', {
        'form': form,
        'room': room
    })

def logout_view(request):
    logout(request)
    return redirect('login')
