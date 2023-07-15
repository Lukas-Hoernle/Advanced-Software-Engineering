from django import forms

from HHPG.application.forms.ProjektForm import ProjektForm
from HHPG.domain.entity.haushaltsposten import Haushaltsposten
from HHPG.domain.entity.projekt import Projekt


class HaushaltspostenForm(forms.ModelForm):
    projekte = forms.inlineformset_factory(
        parent_model=Haushaltsposten,
        model=Projekt,
        form=ProjektForm,
        extra=1,
        min_num=1,
        validate_min=True,
    )

    class Meta:
        model = Haushaltsposten
        fields = [
            'haushaltsplan',
            'name'
        ]
