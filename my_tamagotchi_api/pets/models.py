# pets/models.py

from django.db import models

class CustomPet(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    age = models.IntegerField()
    hunger_level = models.IntegerField(default=0)
    happiness_level = models.IntegerField(default=0)

    def __str__(self):
        return self.name
