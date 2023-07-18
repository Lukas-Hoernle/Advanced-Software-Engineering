from django.shortcuts import render, redirect

from HHPG.application.forms.HaushaltsplanForm import HaushaltsplanForm
from HHPG.application.forms.formfactories import HaushaltspostenFormSet, ProjektFormSet, AufwandFormSet
from HHPG.domain.entity.aufwand import Aufwand
from HHPG.domain.entity.haushaltsplan import Haushaltsplan
from HHPG.domain.entity.haushaltsposten import Haushaltsposten
from HHPG.domain.entity.projekt import Projekt


class IndexView:
    @classmethod
    def index(cls, request):
        if request.method == 'POST':
            haushaltsplan_form = HaushaltsplanForm(request.POST)
            formset = HaushaltspostenFormSet(request.POST, instance=haushaltsplan_form.instance)
            if haushaltsplan_form.is_valid() and formset.is_valid():
                haushaltsplan = haushaltsplan_form.save()
                formset.save()
                return redirect('anzeige', haushaltsplan.id)
        else:
            haushaltsplan_form = HaushaltsplanForm()
            formset = HaushaltspostenFormSet()

        return render(request, 'test.html', {
            'haushaltsplan_form': haushaltsplan_form,
            'formset': formset,
        })


    @classmethod
    def anzeige(cls, request, haushaltsplan_id):
        haushaltsplan = Haushaltsplan.objects.get(id=haushaltsplan_id)
        haushaltsplan.haushaltsposten_liste = Haushaltsposten.objects.filter(haushaltsplan_id=haushaltsplan.id)
        for haushaltsposten in haushaltsplan.haushaltsposten_liste:
            haushaltsposten.projekte = Projekt.objects.filter(haushaltsposten_id=haushaltsposten.id)
            for projekt in haushaltsposten.projekte:
                projekt.aufwand = Aufwand.objects.filter(projekt_id=projekt.id)

        context = {
            'haushaltsplan': haushaltsplan,
        }

        return render(request, 'anzeigen.html', context)

    @classmethod
    def generate_xl(cls, request, haushaltsplan_id):
        # stuff
        # save excel in folder / file idk
        return #file path to excel

