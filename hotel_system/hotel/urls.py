from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_welcome, name='hotel_welcome'),
    path('customer-dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('rooms/', views.roomList, name='room_list'),
]