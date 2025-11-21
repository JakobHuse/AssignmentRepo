from django.shortcuts import render, redirect
from .forms import MoodForm
from .models import mood_entry
from django.contrib.auth import get_user_model

# Create your views here.
def mood_home_view(request):
    return render(request, "mood/home.html")

def add_mood_entry(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            mood_instance = form.save(commit=False)
            mood_instance.user = request.user            
            mood_instance.save() # Saves the new item to the database
            return redirect('mood:home') # Redirect to a view displaying the list
    else:
        form = MoodForm()
        return render(request, 'mood/add_entry.html', {'form': form})


def mood_list(request):
    items = mood_entry.objects.filter(user=request.user) # Fetch all existing items for display
    return render(request, 'mood/entry_list.html', {'items': items})

def entry_detail(request, id):
    mood = mood_entry.objects.get(id=id)
    return render(request, 'mood/entry_detail.html', {'mood': mood})