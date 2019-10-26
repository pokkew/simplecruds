from django.shortcuts import render
from django.forms import ModelForm


def home(request):
    return render(request, "home.html")
