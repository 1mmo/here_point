from django.urls import path

from .views import HerePointLoginView, HerePointLogoutView
from .views import index, profile


app_name = 'users'
urlpatterns = [
    path('profile/', profile, name='profile'),
    path('login/', HerePointLoginView.as_view(), name='login'),
    path('logout/', HerePointLogoutView.as_view(), name='logout'),
]
