from django.urls import path

from .views import HerePointLoginView, HerePointLogoutView, ChangeUserInfoView, RegisterDoneView, RegisterUserView
from .views import index, profile


app_name = 'users'
urlpatterns = [
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('register/', RegisterUserView.as_view (), name='register'),
    path('profile/', profile, name='profile'),
    path('login/', HerePointLoginView.as_view(), name='login'),
    path('logout/', HerePointLogoutView.as_view(), name='logout'),
    path('profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
]