from django.forms import formset_factory

from HHPG.domain.entity.aufwand import Aufwand
from django import forms


class AufwandForm(forms.ModelForm):
    class Meta:
        model = Aufwand
        fields = [
            "einnahmen",
            "ausgaben"
        ]


AufwandFormSet = formset_factory(
    AufwandForm,
    min_num=1,
    can_delete=True
)