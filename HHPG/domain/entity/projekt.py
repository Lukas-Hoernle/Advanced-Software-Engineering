from django.db import models
from HHPG.domain.entity.haushaltsposten import Haushaltsposten


class Projekt(models.Model):
    projekt_name = models.CharField(
        blank=False,
        null=False,
        max_length=255
    )
    haushaltsposten = models.ForeignKey(
        Haushaltsposten,
        on_delete=models.CASCADE,
        null=False
    )

    def __str__(self):
        return self.projekt_name
