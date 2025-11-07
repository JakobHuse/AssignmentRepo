from django import forms
from .models import patient_medication

class MedicationForm(forms.ModelForm):
    class Meta:
        model = patient_medication
        fields = ['name', 'dosage', 'description']
