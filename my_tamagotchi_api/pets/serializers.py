# pets/serializers.py

from rest_framework import serializers
from .models import CustomPet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPet
        fields = ['id', 'name', 'species', 'age', 'hunger_level', 'happiness_level']
