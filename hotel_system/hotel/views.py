from django.shortcuts import render, redirect
from .models import Room, Profile
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user:
                login(request, user)

                # STAFF (admin user)
                if user.is_staff:
                    return redirect('dashboard')

                profile = Profile.objects.filter(user=user).first()

                if profile and profile.role == "teacher":
                    return redirect('teacher_dashboard')

                return redirect('student_dashboard')



    return render(request, 'login.html', {'form': form})

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

@login_required
def roomList(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }
    return render(request, 'room_list.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')