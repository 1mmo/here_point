from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class HerePointLogoutView(LoginRequiredMixin, LogoutView):
    """ Controller-class doing the logout"""
    template_name = 'users/logout.html'
    

class HerePointLoginView(LoginView):
    """ Controller-class doing the login """
    template_name = 'users/login.html'

def index(request):
    """ Main page """
    return render(request, 'users/index.html')

@login_required
# login_required checking users for registration
def profile(request):
    """ Controller-class that display the user profile page """
    return render(request, 'users/profile.html')
