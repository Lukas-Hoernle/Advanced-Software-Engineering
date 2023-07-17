from django import forms

from HHPG.domain.entity.haushaltsplan import Haushaltsplan


class HaushaltsplanForm(forms.ModelForm):
    class Meta:
        model = Haushaltsplan
        fields = [
            'name',
            'standort',
            'startjahr',
            'autor',
            'studierendenzahl'
        ]

