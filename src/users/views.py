from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib import messages
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from .models import AdvUser
from main.models import Place
from .forms import ChangeUserInfoForm, RegisterUserForm, PlaceForm, AIFormSet


@login_required
def profile_place_change(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        form = PlaceForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            place = form.save()
            formset = AIFormSet(request.POST, request.FILES, instance=place)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Объявление исправлено')
                return redirect('users:profile')
    else:
        form = PlaceForm(instance=place)
        formset = AIFormSet(instance=place)
    context = {'form': form, 'formset': formset}
    return render(request, 'users/place_change.html', context)

@login_required
def profile_place_delete(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        place.delete()
        return redirect('users:profile')
    else:
        context = {'place': place}
        return render(request, 'users/place_delete.html', context)

@login_required
def profile_place_add(request):
    if request.method == "POST":
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            place = form.save()
            formset = AIFormSet(request.POST, request.FILES, instance=place)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Место добавлено')
                return redirect('users:profile')
    else:
        form = PlaceForm(initial={'author': request.user.pk})
        formset = AIFormSet()
    context = {'form': form, 'formset': formset}
    return render(request, 'users/add_place.html', context)


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


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('main:index')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS,
                            'Пользователь удален')
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class RegisterUserView(CreateView):
    """ Controller-class rigister new users """
    model = AdvUser
    template_name = 'users/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('users:register_done')


class RegisterDoneView(TemplateView):
    """ Controller-class open pattern after registration """
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

@login_required
# login_required checking users for registration
def profile(request):
    """ Controller-class that display the user profile page """
    places = Place.objects.filter(author=request.user.pk)
    context = {'places': places}
    return render(request, 'users/profile.html', context)
