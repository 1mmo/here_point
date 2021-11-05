from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from .models import AdvUser
from .forms import ChangeUserInfoForm, RegisterUserForm


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Controller-class change UserInfo """
    model = AdvUser
    template_name = 'users/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy("users:profile")
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'users/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('users:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'users/register_done.html'


class HerePointPasswordChangeView(
                SuccessMessageMixin, 
                LoginRequiredMixin,
                PasswordChangeView):
    """ Controller-class change user's password """
    template_name = 'users/password_change.html'
    success_url = reverse_lazy("users:profile")

class HerePointLogoutView(LoginRequiredMixin, LogoutView):
    """ Controller-class doing the logout"""
    template_name = 'users/logout.html'
    next_page = 'main:index'


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
