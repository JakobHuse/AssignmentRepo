from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MedicationForm
from .models import patient_medication
from django.contrib.auth import get_user_model


# Create your views here.
def medication_home_view(request):    
    items = patient_medication.objects.filter(user=request.user) # Fetch all existing items for display
    return render(request, "medication/home.html", {'items': items})

def add_medication(request):
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            medication_instance = form.save(commit=False)
            medication_instance.user = request.user            
            medication_instance.save() # Saves the new item to the database
            return redirect('medication:home') # Redirect to a view displaying the list
    else:
        form = MedicationForm()
    
    items = patient_medication.objects.filter(user=request.user) # Fetch all existing items for display
    return render(request, 'medication/add_item.html', {'form': form, 'items': items})

def medication_detail(request, id):
    medication = patient_medication.objects.get(id=id)
    return render(request, 'medication/medication_details.html', {'medication': medication})

#def delete_medication(request):
    