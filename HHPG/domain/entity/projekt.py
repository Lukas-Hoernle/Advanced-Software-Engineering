from django.contrib.auth.models import User
from django.db import models

from HHPG.domain.entity.haushaltsposten import Haushaltsposten


class Projekt(models.Model):
    haushaltsposten = models.ForeignKey(Haushaltsposten, on_delete=models.CASCADE)
    name = models.CharField(blank=False, null=False, max_length=255)
    einnahmen = models.PositiveIntegerField(blank=False, null=False, default= 0)
    ausgaben = models.PositiveIntegerField(blank=False, null=False, default= 0)

    def __str__(self):
        return f'{self.name} - Einnahmen: {self.einnahmen} - Ausgaben: {self.ausgaben}'
