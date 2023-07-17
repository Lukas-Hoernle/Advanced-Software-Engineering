from django.forms import inlineformset_factory
from django.http import HttpResponse, HttpResponseBadRequest

from HHPG.application.forms.AufwandForm import AufwandForm
from HHPG.application.forms.HaushaltsplanForm import HaushaltsplanForm
from django.shortcuts import render

from HHPG.application.forms.ProjektForm import ProjektForm
from HHPG.application.forms.formfactories import HaushaltspostenFormSet, HaushaltsplanFormSet
from HHPG.domain.entity.haushaltsplan import Haushaltsplan
from HHPG.domain.entity.haushaltsposten import Haushaltsposten
from HHPG.domain.entity.projekt import Projekt


class IndexView:
    @classmethod
    def index(cls, request):
        if request.method != 'POST':
            haushaltsplan_formset = HaushaltsplanFormSet(prefix='haushaltsplan')
            haushaltsposten_formset = HaushaltspostenFormSet(prefix='haushaltsposten')
            projekt_formset = ProjektForm(prefix='projekt')
            aufwand_formset = AufwandForm(prefix='aufwand')
            return render(request, 'test3t.html', {
                'haushaltsplan_formset': haushaltsplan_formset,
                'haushaltsposten_formset': haushaltsposten_formset,
                'projekt_formset': projekt_formset,
                'aufwand_formset': aufwand_formset
            })
        else:
            haushaltsplan_formset = HaushaltsplanFormSet(request.POST, prefix='haushaltsplan')
            if not haushaltsplan_formset.is_valid():
                return HttpResponseBadRequest("Invalid haushaltsplan form")

            haushaltsplan_instance = haushaltsplan_formset.save()
            haushaltsposten_formset = HaushaltspostenFormSet(
                request.POST,
                instance=haushaltsplan_instance,
                prefix='haushaltsposten'
            )

            if not haushaltsposten_formset.is_valid():
                return HttpResponseBadRequest("Invalid haushaltsposten form")

            haushaltsposten_instance = haushaltsposten_formset.save()
            projekt_formset = ProjektForm(request.POST, instance=haushaltsposten_instance,
                                             prefix='projekt')
            if not projekt_formset.is_valid():
                return HttpResponseBadRequest("Invalid projekt form")

            projekt_instance = projekt_formset.save()
            aufwand_formset = AufwandForm(request.POST, instance=projekt_instance, prefix='aufwand')

            if not aufwand_formset.is_valid():
                return HttpResponseBadRequest("Invalid aufwand form")

            aufwand_instance = aufwand_formset.save()
            return HttpResponse("Data saved successfully!")
