from django.urls import path

from .views import (HerePointLoginView, HerePointLogoutView, 
                    ChangeUserInfoView, RegisterDoneView, 
                    RegisterUserView, HerePointPasswordChangeView,
                    DeleteUserView)
from .views import profile, profile_place_add


app_name = 'users'
urlpatterns = [
    path('profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('register/', RegisterUserView.as_view (), name='register'),
    path('profile/add/', profile_place_add, name='profile_place_add'),
    path('profile/', profile, name='profile'),
    path('login/', HerePointLoginView.as_view(), name='login'),
    path('logout/', HerePointLogoutView.as_view(), name='logout'),
    path('profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('profile/password/change/', 
         HerePointPasswordChangeView.as_view(),
         name='password_change'),
]
