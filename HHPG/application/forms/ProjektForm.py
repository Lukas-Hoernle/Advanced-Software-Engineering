from django import forms
from django.forms import formset_factory
from HHPG.application.forms.AufwandForm import AufwandForm
from HHPG.domain.entity.projekt import Projekt


class ProjektForm(forms.ModelForm):
    aufwand = forms.inlineformset_factory(AufwandForm)

    class Meta:
        model = Projekt
        fields = [
            'name',
            'aufwand'
        ]