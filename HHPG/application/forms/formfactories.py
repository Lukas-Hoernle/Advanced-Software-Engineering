from django.forms import inlineformset_factory, BaseInlineFormSet

from HHPG.application.forms.AufwandForm import AufwandForm
from HHPG.domain.entity.aufwand import Aufwand
from HHPG.domain.entity.haushaltsplan import Haushaltsplan
from HHPG.domain.entity.haushaltsposten import Haushaltsposten
from HHPG.domain.entity.projekt import Projekt


class BaseHaushaltspostenFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super(BaseHaushaltspostenFormSet, self).add_fields(form, index)

        # save the formset in the 'nested' property
        form.nested = ProjektFormSet(
            instance=form.instance,
            data=form.data if form.is_bound else None,
            files=form.files if form.is_bound else None,
            prefix='haushaltsposten-%s-%s' % (
                form.prefix,
                ProjektFormSet.get_default_prefix())
        )


class BaseProjektFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super(BaseProjektFormSet, self).add_fields(form, index)

        # save the formset in the 'nested' property
        form.nested = AufwandFormSet(
            instance=form.instance,
            data=form.data if form.is_bound else None,
            files=form.files if form.is_bound else None,
            prefix='projekt-%s-%s' % (
                form.prefix,
                AufwandFormSet.get_default_prefix())
        )


HaushaltspostenFormSet = inlineformset_factory(
    Haushaltsplan,
    Haushaltsposten,
    formset=BaseHaushaltspostenFormSet,
    fields=[
        'posten_name'
    ],
    extra=1,
)

ProjektFormSet = inlineformset_factory(
    Haushaltsposten,
    Projekt,
    formset=BaseProjektFormSet,
    fields=[
        'projekt_name'
    ],
    extra=1,
    can_delete=False
)

AufwandFormSet = inlineformset_factory(
    Projekt,
    Aufwand,
    form=AufwandForm,
    extra=1,
    can_delete=False
)
