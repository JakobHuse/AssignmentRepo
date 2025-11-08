from django import forms 
from django.forms.widgets import Textarea
from .models import patient_medication

class MedicationForm(forms.ModelForm):
    class Meta:
        model = patient_medication
        fields = ['name', 'dosage', 'description', 'frequency', 'reminder_type']
        widgets = {
            'description': Textarea(attrs={'rows':10, 'cols':40}),
        }
