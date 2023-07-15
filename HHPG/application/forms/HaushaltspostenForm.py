from django import forms
from django.forms import formset_factory

from HHPG.application.forms.ProjektForm import ProjektForm
from HHPG.domain.entity.haushaltsposten import Haushaltsposten


class HaushaltspostenForm(forms.ModelForm):
    projekte = formset_factory(
        ProjektForm,
        extra=1,
        min_num=1
    )

    class Meta:
        model = Haushaltsposten
        fields = [
            'name'
        ]
