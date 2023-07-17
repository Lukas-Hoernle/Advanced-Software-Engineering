from django.db import models

from HHPG.domain.entity.projekt import Projekt


class Aufwand(models.Model):
    einnahmen = models.PositiveIntegerField(
        blank=False,
        null=False
    )
    ausgaben = models.PositiveIntegerField(
        blank=False,
        null=False
    )
    projekt = models.ForeignKey(
        Projekt,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        display_name = f"E: {self.einnahmen} A:{self.ausgaben}"
        return display_name
