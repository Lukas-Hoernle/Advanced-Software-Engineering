from django.shortcuts import render

# Abstract Factory Pattern
class FormFactory:
    def create_haushaltsplan_form(self, data=None):
        pass

    def create_haushaltsposten_formset(self, data=None, prefix=None):
        pass

    def create_projekt_formset(self, data=None, prefix=None):
        pass

class DefaultFormFactory(FormFactory):
    def create_haushaltsplan_form(self, data=None):
        return HaushaltsplanForm(data=data)

    def create_haushaltsposten_formset(self, data=None, prefix=None):
        return HaushaltspostenFormSet(data=data, prefix=prefix)

    def create_projekt_formset(self, data=None, prefix=None):
        return ProjektFormSet(data=data, prefix=prefix)

# Strategy Pattern
class HaushaltsplanStrategy:
    def handle_post_request(self, haushaltsplan, haushaltsposten_list):
        pass

class ExcelExportStrategy(HaushaltsplanStrategy):
    def handle_post_request(self, haushaltsplan, haushaltsposten_list):
        excel_generator = HaushaltsplanExcelGenerator(haushaltsplan)
        excel_generator.generate_excel('haushaltsplan.xlsx')
        return render(request, 'success.html')

class HaushaltsplanView:
    def __init__(self, form_factory):
        self.form_factory = form_factory

    def handle_post_request(self, request):
        haushaltsplan_form = self.form_factory.create_haushaltsplan_form(request.POST)
        haushaltsposten_formset = self.form_factory.create_haushaltsposten_formset(request.POST, prefix='haushaltsposten')
        projekt_formset = self.form_factory.create_projekt_formset(request.POST, prefix='projekt')

        if haushaltsplan_form.is_valid() and haushaltsposten_formset.is_valid() and projekt_formset.is_valid():
            haushaltsplan = haushaltsplan_form.save()
            haushaltsposten_list = []

            for haushaltsposten_form in haushaltsposten_formset:
                haushaltsposten = haushaltsposten_form.save(commit=False)
                haushaltsposten.haushaltsplan = haushaltsplan
                haushaltsposten.save()
                projekt_list = []

                for projekt_form in projekt_formset:
                    projekt = projekt_form.save(commit=False)
                    projekt.haushaltsposten = haushaltsposten

                    einnahmen = 0
                    ausgaben = 0
                    aufwand = projekt.aufwand

                    if aufwand:
                        einnahmen = aufwand.einnahmen
                        ausgaben = aufwand.ausgaben

                    projekt.einnahmen = einnahmen
                    projekt.ausgaben = ausgaben
                    projekt.save()
                    projekt_list.append(projekt)

                haushaltsposten.projekte.set(projekt_list)
                haushaltsposten_list.append(haushaltsposten)

            haushaltsplan.haushaltsposten.set(haushaltsposten_list)

            # Strategy Pattern
            strategy = ExcelExportStrategy()
            return strategy.handle_post_request(haushaltsplan, haushaltsposten_list)

    def handle_get_request(self, request):
        haushaltsplan_form = self.form_factory.create_haushaltsplan_form()
        haushaltsposten_formset = self.form_factory.create_haushaltsposten_formset(prefix='haushaltsposten')
        projekt_formset = self.form_factory.create_projekt_formset(prefix='projekt')

        context = {
            'haushaltsplan_form': haushaltsplan_form,
            'haushaltsposten_formset': haushaltsposten_formset,
            'projekt_formset': projekt_formset,
        }

        return render(request, 'create_haushaltsplan.html', context)

def create_haushaltsplan(request):
    form_factory = DefaultFormFactory()
    view = HaushaltsplanView(form_factory)

    if request.method == 'POST':
        return view.handle_post_request(request)
    else:
        return view.handle_get_request(request)
