from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CreateUserForm

# Create your views here.
class SignUpView(CreateView):
    form_class = CreateUserForm #extends CreateView and sets form to CreateUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"