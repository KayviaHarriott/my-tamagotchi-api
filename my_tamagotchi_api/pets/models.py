from django.db import models
from django.contrib.postgres.fields import ArrayField

class CustomPet(models.Model):
    class PetStatus(models.TextChoices):
        DEAD = 'DEAD', 'Dead'
        ALIVE = 'ALIVE', 'Alive'

    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    age = models.IntegerField()
    status = models.CharField(max_length=5, choices=PetStatus.choices, default=PetStatus.ALIVE)
    health_level = models.IntegerField(default=0) # max 100
    hunger_level = models.IntegerField(default=0) # max 100
    happiness_level = models.IntegerField(default=0) # max 100
    thirst_level = models.IntegerField(default=0) # max 100
    bathroom_level = models.IntegerField(default=0) # max 100
    friendliness = models.IntegerField(default=0) # max 100
    # likes = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    # dislikes = ArrayField(models.CharField(max_length=255), blank=True, default=list)



    def __str__(self):
        return self.name
