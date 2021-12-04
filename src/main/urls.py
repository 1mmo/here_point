from django.urls import path

from .views import index, by_category, detail


app_name = 'main'
urlpatterns = [
    # path('accounts/login/', HerePointLoginView.as_view(), name='login'),
    path('', index, name='index'),
    path('<int:category_pk>/<int:pk>/', detail, name='detail'),
    path('<int:pk>/', by_category, name='by_category'),
]
