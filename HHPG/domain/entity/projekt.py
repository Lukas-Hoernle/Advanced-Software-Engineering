from django.db import models
from HHPG.domain.entity.aufwand import Aufwand
from HHPG.domain.entity.haushaltsposten import Haushaltsposten


class Projekt(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=255
    )
    haushaltsposten = models.ForeignKey(
        Haushaltsposten,
        on_delete=models.CASCADE,
        null=False
    )
    aufwand = models.ForeignKey(
        Aufwand,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name
