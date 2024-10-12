
from django.urls import path
from .views import OfferListCreateView, OfferDetailView

urlpatterns = [
    path('', OfferListCreateView.as_view(), name='offer_list_create'),  # Esto será accedido por 'api/offers/'
    path('<int:pk>/', OfferDetailView.as_view(), name='offer_detail'),
]

