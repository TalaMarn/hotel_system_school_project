from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_dashboard, name='customer_dashboard'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('rooms/', views.roomList, name='room_list'),
    path('booking/<int:room_id>/', views.booking_view, name='booking'),
    
]