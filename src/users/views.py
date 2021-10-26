from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


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
