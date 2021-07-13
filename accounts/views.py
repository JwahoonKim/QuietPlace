import accounts
from django.shortcuts import render, redirect

# Create your views here.


def signup(request):
    return render(request, 'accounts/signup.html')


def login(request):
    return render(request, 'accounts/login.html')


def revise(request):
    return render(request, 'accounts/revise.html')
