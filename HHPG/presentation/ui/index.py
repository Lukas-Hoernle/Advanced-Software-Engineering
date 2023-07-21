from django.contrib import messages
from django.shortcuts import render, redirect

from HHPG.application.HaushaltsplanExcelGenerator import HaushaltsplanExcelGenerator
from HHPG.application.budget_berechner import BudgetBerechner
from HHPG.application.forms.HaushaltsplanForm import HaushaltsplanForm
from HHPG.application.forms.formfactories import HaushaltspostenFormSet
from HHPG.domain.entity.aufwand import Aufwand
from HHPG.domain.entity.haushaltsposten import Haushaltsposten
from HHPG.domain.entity.projekt import Projekt
from HHPG.infrastruktur.haushaltsplan_repository import HaushaltsplanRepository
from HHPG.infrastruktur.haushaltsposten_repository import HaushaltspostenRepository
from HHPG.infrastruktur.projekt_repository import ProjektRepository


class IndexView:
    haushaltsplan_repository = HaushaltsplanRepository()
    haushaltsposten_repository = HaushaltspostenRepository()
    projekt_repository = ProjektRepository()

    @classmethod
    def index(cls, request):
        if request.method == 'POST':
            haushaltsplan_form = HaushaltsplanForm(request.POST)
            formset = HaushaltspostenFormSet(request.POST, instance=haushaltsplan_form.instance)
            if haushaltsplan_form.is_valid() and formset.is_valid():
                haushaltsplan = haushaltsplan_form.save()
                formset.save(request=request)
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
        haushaltsplan = cls.haushaltsplan_repository.get_by_id_including_children(haushaltsplan_id=haushaltsplan_id)

        if len(messages.get_messages(request)) < 1:
            budget, ausgaben = BudgetBerechner(haushaltsplan=haushaltsplan).ist_verlustbehaftet()

            if ausgaben > budget:
                message = f'ÜBERSCHRITTEN von {budget - ausgaben}€!! BUDGET: {budget}, AUSGABEN:{ausgaben}'
                messages.warning(request, message)

        HaushaltsplanExcelGenerator(haushaltsplan=haushaltsplan).generate_excel("testing.xls")
        context = {
            'haushaltsplan': haushaltsplan,
        }

        return render(request, 'anzeigen.html', context)

    @classmethod
    def generate_xl(cls, request, haushaltsplan_id):
        # stuff
        # save excel in folder / file
        return  # file path to excel
