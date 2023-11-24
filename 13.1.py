from django.db import models

class Sword(models.Model):
    name = models.CharField(max_length=100)
    damage = models.IntegerField()
    rarity = models.CharField(max_length=50)
