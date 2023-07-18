from django import forms

from HHPG.domain.entity.haushaltsplan import Haushaltsplan


class HaushaltsplanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HaushaltsplanForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Haushaltsplan
        fields = [
            'plan_name',
            'standort',
            'startjahr',
            'author',
            'studierendenzahl'
        ]

