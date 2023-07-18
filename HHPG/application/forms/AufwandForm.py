from HHPG.domain.entity.aufwand import Aufwand
from django import forms


class AufwandForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AufwandForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Aufwand
        fields = [
            "einnahmen",
            "ausgaben"
        ]
