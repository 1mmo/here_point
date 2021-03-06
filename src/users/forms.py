from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


from .models import AdvUser
from main.models import Place, AdditionalImage


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
        widgets = {'author': forms.HiddenInput}

AIFormSet = inlineformset_factory(Place, AdditionalImage, fields='__all__')


class ChangeUserInfoForm(forms.ModelForm):
    """ Form for change main info about user """
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    username = forms.CharField(max_length=15, required=True, label='Никнейм')
    first_name = forms.CharField(max_length=15, required=True, label='Имя')
    last_name = forms.CharField(max_length=15, required=True, label='Фамилия')
    
    class Meta:
        model = AdvUser
        fields = ('email', 'username', 'first_name', 
                  'last_name', 'send_messages')


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    username = forms.CharField(max_length=15, required=True, label='Никнейм')
    first_name = forms.CharField(max_length=15, required=True, label='Имя')
    last_name = forms.CharField(max_length=15, required=True, label='Фамилия')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput,
            help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (повторно)',
            widget=forms.PasswordInput,
            help_text='Повторите пароль')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        try:
            password_validation.validate_password(password1)
        except forms.ValidationError as error:
            self.add_error('password1', error)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
            'ВВеденные пароли не совпадают', code='password_mismath' )}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True        
        if commit:
            user.save()
        #user_registered.send(RegisterUserForm, instance=user)
        return user


    class Meta:
        model = AdvUser
        fields = {'username', 'email', 'password1', 'password2',
                  'first_name', 'last_name', 'send_messages'}

