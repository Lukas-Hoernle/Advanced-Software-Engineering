from django import forms
from HHPG.domain.entity.projekt import Projekt


class ProjektForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjektForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Projekt
        fields = [
            'projekt_name'
        ]
