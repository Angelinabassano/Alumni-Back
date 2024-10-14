from django.urls import path
from .views import school_list  # Importa la vista que creaste

urlpatterns = [
    path('schools/', school_list, name='school_list'),  # Define la ruta para las escuelas
]
