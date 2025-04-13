from django import forms
from .models import Booking, Service, Barber

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'barber', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.filter(available=True)
        self.fields['barber'].queryset = Barber.objects.filter(available=True)
