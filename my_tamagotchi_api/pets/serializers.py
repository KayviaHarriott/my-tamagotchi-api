# pets/serializers.py

from rest_framework import serializers
from .models import CustomPet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPet
        fields = [
            'id', 'name', 'species', 'age', 'status', 'health_level',
            'hunger_level', 'thirst_level','happiness_level', 'bathroom_level',
            'friendliness'
            #, 'likes', 'dislikes'
        ]
