from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_home, name='booking_home'),
    path('create/', views.create_booking, name='create_booking'),
    path('manage/', views.manage_bookings, name='manage_bookings'),
]
