from django.urls import path
from .views import UserCreateView, UserUpdateView, LoginView

urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='create_user'),
    path('update/<int:pk>/<str:role>/', UserUpdateView.as_view(), name='user_update'),
    path('login/', LoginView.as_view(), name='login'),
]