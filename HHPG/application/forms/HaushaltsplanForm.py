from django import forms

from HHPG.domain.entity.haushaltsplan import Haushaltsplan


class HaushaltsplanForm(forms.ModelForm):
    class Meta:
        model = Haushaltsplan
        fields = [
            'plan_name',
            'standort',
            'startjahr',
            'author',
            'studierendenzahl'
        ]

