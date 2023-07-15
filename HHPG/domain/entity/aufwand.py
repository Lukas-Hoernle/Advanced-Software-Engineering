from django.db import models


class Aufwand(models.Model):
    einnahmen = models.PositiveIntegerField(
        blank=False,
        null=False
    )
    ausgaben = models.PositiveIntegerField(
        blank=False,
        null=False
    )

    def __str__(self):
        display_name = f"E: {self.einnahmen} A:{self.ausgaben}"
        return display_name
