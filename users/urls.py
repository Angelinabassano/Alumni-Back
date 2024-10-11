from django.urls import path
from .views import UserCreateView
from .views import LoginView


urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='login'),

]


