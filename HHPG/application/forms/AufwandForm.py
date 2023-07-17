from HHPG.domain.entity.aufwand import Aufwand
from django import forms


class AufwandForm(forms.ModelForm):
    class Meta:
        model = Aufwand
        fields = [
            "einnahmen",
            "ausgaben"
        ]
