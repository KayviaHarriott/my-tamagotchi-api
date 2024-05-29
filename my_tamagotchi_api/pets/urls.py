from django.urls import path
from .views import PetListCreateView, PetRetrieveUpdateDestroyView, PetDetailView

urlpatterns = [
    path('pets/', PetListCreateView.as_view(), name='pet-list-create'),
    path('pets/<int:pk>/', PetRetrieveUpdateDestroyView.as_view(), name='pet-detail'),
    path('api/pets/<int:pk>/', PetDetailView.as_view(), name='pet-detail-api'),
]
