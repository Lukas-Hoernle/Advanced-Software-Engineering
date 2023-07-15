from django import forms
from django.forms import formset_factory
from HHPG.domain.entity.projekt import Projekt


class ProjektForm(forms.ModelForm):
    class Meta:
        model = Projekt
        fields = [
            'name',
            'aufwand'
        ]


ProjektFormSet = formset_factory(
    ProjektForm,
    min_num=1,
    can_delete=True
)
