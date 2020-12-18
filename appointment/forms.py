from django import forms
from .models import Appointment

class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('appointment_date',)
    
        widgets = {
            'appointment_date': forms.DateTimeField(),
        }
