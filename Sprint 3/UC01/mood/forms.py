from django import forms 
from django.forms.widgets import Textarea
from .models import mood_entry

class MoodForm(forms.ModelForm):
    class Meta:
        model = mood_entry
        fields = ['date', 'description']
        widgets = {
            'description': Textarea(attrs={'rows':10, 'cols':40}),
            'date': forms.SelectDateWidget()
        }
