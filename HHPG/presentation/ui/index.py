from django.forms import inlineformset_factory

from HHPG.application.forms.HaushaltsplanForm import HaushaltsplanForm
from django.shortcuts import render
from HHPG.domain.entity.haushaltsplan import Haushaltsplan
from HHPG.domain.entity.haushaltsposten import Haushaltsposten
from HHPG.domain.entity.projekt import Projekt


class IndexView:
    @classmethod
    def index(cls, request):
        HaushaltspostenFormSet = inlineformset_factory(
            Haushaltsplan,
            Haushaltsposten,
            fields=('name',),
            extra=1,
            can_delete=True
        )

        ProjektFormSet = inlineformset_factory(
            Haushaltsposten,
            Projekt,
            fields=('name', 'aufwand'),
            extra=1,
            can_delete=True
        )

        if request.method == 'POST':
            haushaltsplan_form = HaushaltsplanForm(request.POST)
            haushaltsposten_formset = HaushaltspostenFormSet(request.POST, prefix='haushaltsposten')
            projekt_formset = ProjektFormSet(request.POST, prefix='projekt')

            if haushaltsplan_form.is_valid() and haushaltsposten_formset.is_valid() and projekt_formset.is_valid():
                haushaltsplan = haushaltsplan_form.save()
                haushaltsposten_formset.instance = haushaltsplan
                haushaltsposten_formset.save()
                projekt_formset.save()

        else:
            haushaltsplan_form = HaushaltsplanForm()
            haushaltsposten_formset = HaushaltspostenFormSet(prefix='haushaltsposten')
            projekt_formset = ProjektFormSet(prefix='projekt')

        return render(request, 'test.html', {
            'haushaltsplan_form': haushaltsplan_form,
            'haushaltsposten_formset': haushaltsposten_formset,
            'projekt_formset': projekt_formset,
        })

