from django import forms

from HHPG.application.forms.AufwandForm import AufwandForm
from HHPG.domain.entity.projekt import Projekt


class ProjektForm(forms.ModelForm):
    aufwand = AufwandForm()

    class Meta:
        model = Projekt
        fields = [
            'name',
            'haushaltsposten',
            'aufwand'
        ]