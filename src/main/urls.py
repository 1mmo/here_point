from django.urls import path

from .views import index


app_name = 'main'
urlpatterns = [
    # path('accounts/login/', HerePointLoginView.as_view(), name='login'),
    path('', index, name='index'),
]
