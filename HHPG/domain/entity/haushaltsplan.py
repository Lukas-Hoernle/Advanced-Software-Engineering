from django.contrib.auth.models import User
from django.db import models



class Haushaltsplan(models.Model):
    plan_name = models.CharField(blank=False, null=False, max_length=255)
    standort = models.CharField(
        choices=[
            ('Heidenheim', 'Heidenheim'),
            ('Heilbronn', 'Heilbronn'),
            ('Karlsruhe', 'Karlsruhe'),
            ('Lörrach', 'Lörrach'),
            ('Mannheim', 'Mannheim'),
            ('Mosbach', 'Mosbach'),
            ('Bad Mergentheim', 'Bad Mergentheim'),
            ('Ravensburg', 'Ravensburg'),
            ('Friedrichshafen', 'Friedrichshafen'),
            ('Stuttgart / Horb', 'Stuttgart / Horb'),
            ('Villingen-Schwenningen', 'Villingen-Schwenningen'),
        ],
        blank=False,
        null=False,
        max_length=255
    )
    startjahr = models.PositiveIntegerField(
        blank=False,
        null=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True
    )
    studierendenzahl = models.PositiveIntegerField(
        blank=False,
        null=False
    )

    def __str__(self):
        return self.plan_name
