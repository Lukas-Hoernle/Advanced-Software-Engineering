from django import forms
from django.forms import inlineformset_factory, BaseInlineFormSet

from HHPG.application.forms.AufwandForm import AufwandForm
from HHPG.application.forms.HaushaltspostenForm import HaushaltspostenForm
from HHPG.application.forms.ProjektForm import ProjektForm
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

    def is_valid(self):
        result = super(BaseHaushaltspostenFormSet, self).is_valid()

        if self.is_bound:
            for form in self.forms:
                if hasattr(form, 'nested'):
                    result = result and form.nested.is_valid()

        return result

    def save(self, commit=True):

        result = super(BaseHaushaltspostenFormSet, self).save(commit=commit)

        for form in self.forms:
            if hasattr(form, 'nested'):
                if not self._should_delete_form(form):
                    form.nested.save(commit=commit)

        return result


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

        def is_valid(self):
            result = super(BaseProjektFormSet, self).is_valid()

            if self.is_bound:
                for form in self.forms:
                    if hasattr(form, 'nested'):
                        result = result and form.nested.is_valid()

            return result

    def save(self, commit=True):

        result = super(BaseProjektFormSet, self).save(commit=commit)

        for form in self.forms:
            if hasattr(form, 'nested'):
                if not self._should_delete_form(form):
                    form.nested.save(commit=commit)

        return result


HaushaltspostenFormSet = inlineformset_factory(
    Haushaltsplan,
    Haushaltsposten,
    form=HaushaltspostenForm,
    formset=BaseHaushaltspostenFormSet,
    fields=[
        'posten_name',
    ],
    extra=1,
    can_delete=False
)

ProjektFormSet = inlineformset_factory(
    Haushaltsposten,
    Projekt,
    form=ProjektForm,
    formset=BaseProjektFormSet,
    fields=[
        'projekt_name',
    ],
    extra=1,
    can_delete=False
)

AufwandFormSet = inlineformset_factory(
    Projekt,
    Aufwand,
    form=AufwandForm,
    extra=1,
    max_num=1,
    can_delete=False
)
