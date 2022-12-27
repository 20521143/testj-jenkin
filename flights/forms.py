from .models import Flight, Passenger, Airport
from django.forms  import ModelForm
from django import forms

class FlightForm(ModelForm):
    
    class Meta:
        model = Flight
        fields = ('origin', 'destination', 'duration')
        
        widgets = {
            'origin': forms.Select(attrs={'class':'form-select', 'placeholder':'origin'}),
            'destination': forms.Select(attrs={'class':'form-select', 'placeholder':'destination'}),
            'duration': forms.TextInput(attrs={'class':'form-control'}),
        }