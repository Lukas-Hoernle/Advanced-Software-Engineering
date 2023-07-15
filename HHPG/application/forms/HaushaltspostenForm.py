from django import forms
from django.forms import formset_factory

from HHPG.application.forms.ProjektForm import ProjektForm
from HHPG.domain.entity.haushaltsposten import Haushaltsposten


class HaushaltspostenForm(forms.ModelForm):

    class Meta:
        model = Haushaltsposten
        fields = [
            'name'
        ]


HaushaltspostenFormSet = formset_factory(
   HaushaltspostenForm,
    extra=1,
    min_num=1
)