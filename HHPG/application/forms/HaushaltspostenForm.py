from django import forms

from HHPG.domain.entity.haushaltsposten import Haushaltsposten


class HaushaltspostenForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HaushaltspostenForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['posten_name'].widget.attrs['onkeyup'] = 'update_title(event);'

    class Meta:
        model = Haushaltsposten
        fields = [
            'posten_name'
        ]
