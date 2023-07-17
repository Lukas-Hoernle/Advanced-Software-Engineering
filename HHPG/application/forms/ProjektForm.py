from django import forms
from HHPG.domain.entity.projekt import Projekt


class ProjektForm(forms.ModelForm):
    class Meta:
        model = Projekt
        fields = [
            'projekt_name'
        ]
