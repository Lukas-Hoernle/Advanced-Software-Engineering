from django import forms

from HHPG.domain.entity.haushaltsposten import Haushaltsposten


class HaushaltspostenForm(forms.ModelForm):

    class Meta:
        model = Haushaltsposten
        fields = [
            'name'
        ]
