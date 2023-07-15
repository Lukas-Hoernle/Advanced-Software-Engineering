from HHPG.infrastruktur.projekt_repository import ProjektRepository
from django.shortcuts import render


class IndexView:
    @classmethod
    def index(cls, request):
        HaushaltspostenFormSet = formset_factory(
            HaushaltspostenForm,
            extra=1
        )
        ProjektFormSet = inlineformset_factory(
            Haushaltsposten,
            Projekt,
            form=ProjektForm,
            extra=1,
            can_delete=False,
            min_num=1
        )

        haushaltsplan_form = HaushaltsplanForm()
        haushaltsposten_formset = HaushaltspostenFormSet(prefix='haushaltsposten')

        context = {
            'haushaltsplan_form': haushaltsplan_form,
            'haushaltsposten_formset': haushaltsposten_formset
        }

        return render(request, 'test.html', context)
