from django.contrib.auth.models import User
from django.db import models

from HHPG.domain.entity.haushaltsplan import Haushaltsplan


class Haushaltsposten(models.Model):
    haushaltsplan = models.ForeignKey(Haushaltsplan, on_delete=models.CASCADE, null=False)
    name = models.CharField(blank=False, null=False, max_length=255)


    def __str__(self):
        return self.name

