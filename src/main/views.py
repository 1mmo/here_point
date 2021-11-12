from django.shortcuts import render
from django.contrib.auth.views import LoginView


def index(request):
    return render(request, 'primary_main.html')
