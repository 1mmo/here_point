from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.views import LoginView


class HerePointLoginView(LoginView):
    template_name = 'users/login.html'

def index(request):
    return render(request, 'users/index.html')

