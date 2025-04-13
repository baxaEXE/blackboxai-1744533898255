from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm

@login_required
def booking_home(request):
    return render(request, 'booking/home.html')

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('manage_bookings')
    else:
        form = BookingForm()
    return render(request, 'booking/create.html', {'form': form})

@login_required
def manage_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/manage.html', {'bookings': bookings})
