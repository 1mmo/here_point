from django.urls import path

from .views import HerePointLoginView
from .views import index, profile


app_name = 'users'
urlpatterns = [
    path('profile/', profile, name='profile'),
    path('login/', HerePointLoginView.as_view(), name='login'),
]
