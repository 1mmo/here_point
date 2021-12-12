from django import forms
from captcha.fields import CaptchaField

from .models import Comment


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('is_active',)
        widgets = {'place': forms.HiddenInput, 'author': forms.HiddenInput}


class GuestCommentForm(forms.ModelForm):
    captcha = CaptchaField(label='Введите текст с картинки',
                           error_messages={'invalid': "Неправильный текст"})
    
    class Meta:
        model = Comment
        exclude = ('is_active', 'author',)
        widgets = {'place': forms.HiddenInput}


class SearchForm(forms.Form):
    keyword = forms.CharField(required=False, max_length=32, label='')
