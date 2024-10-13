from django.urls import path
from .views import UserCreateView, UserUpdateView, CoderListView, EmpresaListView, GetUser, LoginView

urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='create_user'),
    path('update/<int:pk>/<str:role>/', UserUpdateView.as_view(), name='update_user'),
    path('listcoders/', CoderListView.as_view(), name='coder-list'),
    path('listempresas/', EmpresaListView.as_view(), name='coder-list'),
    path('getuser/<int:pk>/<str:role>/', GetUser.as_view(), name='get_user'),
    path('login/', LoginView.as_view(), name='login'),
]

