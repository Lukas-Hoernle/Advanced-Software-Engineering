from django import forms
from django.forms import formset_factory

from HHPG.application.forms.HaushaltspostenForm import HaushaltspostenForm
from HHPG.domain.entity.haushaltsplan import Haushaltsplan
from HHPG.domain.entity.haushaltsposten import Haushaltsposten


class HaushaltsplanForm(forms.ModelForm):
    haushaltsposten = formset_factory(
        HaushaltspostenForm,
        extra=1,
        min_num=1
    )

    class Meta:
        model = Haushaltsplan
        fields = [
            'name',
            'standort',
            'startjahr',
            'autor',
            'studierendenzahl'
        ]
