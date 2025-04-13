from django.contrib import admin
from .models import Service, Barber, Booking

admin.site.register(Service)
admin.site.register(Barber)
admin.site.register(Booking)
