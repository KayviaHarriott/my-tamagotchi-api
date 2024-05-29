# pets/views.py

from rest_framework import generics
from .models import CustomPet
from .serializers import PetSerializer

class PetListCreateView(generics.ListCreateAPIView):
    queryset = CustomPet.objects.all()
    serializer_class = PetSerializer

class PetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomPet.objects.all()
    serializer_class = PetSerializer
