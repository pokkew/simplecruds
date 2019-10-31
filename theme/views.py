from django.shortcuts import render, redirect
from django.forms import ModelForm


def home(request):
    return render(request, "home.html")


def login(request):
    return redirect('/accounts/login/')