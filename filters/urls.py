from django.urls import path
from .views import filter_coders


urlpatterns = [
    path('coders/filter/', filter_coders, name='filter_coders'),
]
