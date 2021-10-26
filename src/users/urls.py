from django.urls import path

from .views import HerePointLoginView
from .views import index


app_name = 'users'
urlpatterns = [
    path('login/', HerePointLoginView.as_view(), name='login'),
]
