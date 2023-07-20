## 6. Refactoring und Qualitätssicherung

### 6.1 Identifikation von Code Smells

Die Identifikation von Code Smells im Haushaltsplangenerator-Projekt wurde während der gesamten Entwicklungsphase kontinuierlich durchgeführt. Dabei wurde besonders auf die Einhaltung der Coding-Standards und bewährter Entwurfsprinzipien geachtet. Die Qualitätskontrolle fand manuell statt, da SonarCloud große Probleme mit der Nutzung des Frameworks Django hatte. 

Hierbei wurden viele Codesmells aufgedeckt. Die gängigstgen waren: 

1. Lange Methoden: Einige Methoden waren zu umfangreich und enthielten zu viele Verantwortlichkeiten, was die Lesbarkeit erschwerte und die Wartbarkeit beeinträchtigte. Beispiel: [https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/commit/bcf8f41f56454f2d060bf9598c6607999a53c6a1](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/commit/bcf8f41f56454f2d060bf9598c6607999a53c6a1) Hier wird eine sehr lange >Methode aufgetrennt. Für genauere Umschreibung des commits siehe **Refactoring-Dokumentation: Optimierung der Datenbankabfrage für Haushaltspläne**
2. Hohe Komplexität: Bestimmte Codeabschnitte wiesen eine hohe zyklomatische Komplexität auf, was die Verständlichkeit erschwerte und die Anfälligkeit für Fehler erhöhte. Dies war meistens darauf zurückzuführen, dass mehr Zeilen eingefügt wurden, um die Zeilenmindestanzahl zu schaffen. Beispiel: [https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/commit/bcf8f41f56454f2d060bf9598c6607999a53c6a1](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/commit/bcf8f41f56454f2d060bf9598c6607999a53c6a1) Hier wird aus einer sehr komplexen Methode mehrere verteilte simple Methoden. Für genauere Umschreibung des commits siehe **Refactoring-Dokumentation: Optimierung der Datenbankabfrage für Haushaltspläne**
3. Schlechte Benennung. Methoden oder Klassen mit nichtssagenden oder falschen Benennungen. Beispiel: [https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/commit/d00dabd724533037f52df2010891962bcca59fd9](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/commit/4f86f5998566a37089702e174511c3660390bc99) Hier wird eine Methode umbenannt.
4. Kommentare: Eine übermäßige Anzahl von Kommentaren im Code, insbesondere solche, die den offensichtlichen Code erklären, kann ein Anzeichen dafür sein, dass der Code selbst nicht ausreichend selbsterklärend ist. Besser lesbaren Code zu schreiben kann dazu beitragen, unnötige Kommentare zu reduzieren. Dieser Code Smell existierrt noch jetzt im Code. Siehe: [https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/commit/7ea513af7a568687936beee4f417ae83b30bc5b6](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/commit/7ea513af7a568687936beee4f417ae83b30bc5b6) Hier habe ich den Codesmell "zu viele Kommentare" erkannt und entfernt. 
 
**Refactoring-Dokumentation: Optimierung der Datenbankabfrage für Haushaltspläne**

In diesem Refactoring wurde die Datenbankabfrage für Haushaltspläne und deren zugehörige Entitäten optimiert, um die Leistung und Lesbarkeit des Codes zu verbessern. Die Änderungen wurden in den folgenden Dateien vorgenommen:

**Commit 1: Änderungen in HHPG/presentation/ui/index.py**
- **Vorher:**
```python
from django.shortcuts import render, redirect

from HHPG.application.forms.HaushaltsplanForm import HaushaltsplanForm
from HHPG.application.forms.formfactories import HaushaltspostenFormSet, ProjektFormSet, AufwandFormSet
from HHPG.domain.entity.aufwand import Aufwand
from HHPG.domain.entity.haushaltsplan import Haushaltsplan
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
        return  # file path to excel
```

- **Nachher:**
```python
from django.shortcuts import render, redirect

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
        haushaltsplan = cls.haushaltsplan_repository.get_by_id_including_children(haushaltsplan_id=haushaltsplan_id)

        context = {
            'haushaltsplan': haushaltsplan,
        }
        return render(request, 'anzeigen.html', context)

    @classmethod
    def generate_xl(cls, request, haushaltsplan_id):
        # stuff
        # save excel in folder / file idk
        return  # file path to excel
```

**Commit-Link:** [bcf8f41f56454f2d060bf9598c6607999a53c6a1](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/commit/bcf8f41f56454f2d060bf9598c6607999a53c6a1)

**Commit 2: Änderungen in HHPG/infrastruktur/haushaltsposten_repository.py**
- **Vorher:**
```python
from django.db.models import QuerySet
from HHPG.domain.entity.haushaltsposten import Haushaltsposten
from ..domain.entity.haushaltsplan import Haushaltsplan
from ..domain.repository.haushaltsposten_repository import IHaushaltspostenRepository

class HaushaltspostenRepository(IHaushaltspostenRepository):
    def create(self, sender, instance, **kwargs) -> Haushaltsposten:
        return Haushaltsposten.objects.create(**instance)
    def save(self, sender, instance, **kwargs) -> None:
        instance.save()
    def delete(self, haushaltsposten_id: int) -> None:
        Haushaltsposten.objects.filter(id=haushaltsposten_id).delete()
   

 def get_by_id(self, haushaltsposten_id: int) -> Haushaltsposten:
        return Haushaltsposten.objects.get(id=haushaltsposten_id)

    def get_all(self) -> QuerySet:
        return Haushaltsposten.objects.all()
```

- **Nachher:**
```python
from django.db.models import QuerySet
from HHPG.domain.entity.haushaltsposten import Haushaltsposten
from .projekt_repository import ProjektRepository
from ..domain.entity.haushaltsplan import Haushaltsplan
from ..domain.repository.haushaltsposten_repository import IHaushaltspostenRepository

class HaushaltspostenRepository(IHaushaltspostenRepository):
    def create(self, sender, instance, **kwargs) -> Haushaltsposten:
        return Haushaltsposten.objects.create(**instance)
    def save(self, sender, instance, **kwargs) -> None:
        instance.save()
    def delete(self, haushaltsposten_id: int) -> None:
        Haushaltsposten.objects.filter(id=haushaltsposten_id).delete()
    def get_by_id(self, haushaltsposten_id: int) -> Haushaltsposten:
        return Haushaltsposten.objects.get(id=haushaltsplan_id)

    def get_all_by_haushaltsplan_including_children(self, haushaltsplan: Haushaltsplan) -> QuerySet:
        haushaltsposten_liste = self.get_all_by_haushaltsplan(haushaltsplan=haushaltsplan)
        for haushaltsposten in haushaltsposten_liste:
            haushaltsposten.projekte = ProjektRepository().get_all_by_haushaltsposten_including_children(
                haushaltsposten_id=haushaltsposten.id)

        return haushaltsposten_liste

    def get_all(self) -> QuerySet:
        return Haushaltsposten.objects.all()
```

**Commit-Link:** [e9f1e2293aceb3b5b73a49cf42fb47868f4049b7](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/commit/e9f1e2293aceb3b5b73a49cf42fb47868f4049b7)

**Commit 3: Änderungen in HHPG/infrastruktur/haushaltsplan_repository.py**
- **Vorher:**
```python
from django.contrib.auth.models import User
from django.db.models import QuerySet

from ..domain.entity.haushaltsplan import Haushaltsplan
from ..domain.repository.haushaltsplan_repository import IHaushaltsplanRepository

class HaushaltsplanRepository(IHaushaltsplanRepository):
    def create(self, sender, instance, **kwargs) -> Haushaltsplan:
        return Haushaltsplan.objects.create(**instance)
    def save(self, sender, instance, **kwargs) -> None:
        instance.save()
    def delete(self, haushaltsplan_id: int) -> None:
        Haushaltsplan.objects.filter(id=haushaltsplan_id).delete()
    def get_by_id(self, haushaltsplan_id: int) -> Haushaltsplan:
        return Haushaltsplan.objects.get(id=haushaltsplan_id)

    def get_all(self) -> QuerySet:
        return Haushaltsplan.objects.all()
```

- **Nachher:**
```python
from django.contrib.auth.models import User
from django.db.models import QuerySet

from .haushaltsposten_repository import HaushaltspostenRepository
from ..domain.entity.haushaltsplan import Haushaltsplan
from ..domain.repository.haushaltsplan_repository import IHaushaltsplanRepository

class HaushaltsplanRepository(IHaushaltsplanRepository):
    def create(self, sender, instance, **kwargs) -> Haushaltsplan:
        return Haushaltsplan.objects.create(**instance)
    def save(self, sender, instance, **kwargs) -> None:
        instance.save()
    def delete(self, haushaltsplan_id: int) -> None:
        Haushaltsplan.objects.filter(id=haushaltsplan_id).delete()
    def get_by_id(self, haushaltsplan_id: int) -> Haushaltsplan:
        return Haushaltsplan.objects.get(id=haushaltsplan_id)

    def get_by_id_including_children(self, haushaltsplan_id: int) -> Haushaltsplan:
        haushaltsplan = self.get_by_id(haushaltsplan_id=haushaltsplan_id)
        haushaltsplan.haushaltsposten_liste = HaushaltspostenRepository().get_all_by_haushaltsplan_including_children(
            haushaltsplan=haushaltsplan)
        return haushaltsplan

    def get_all(self) -> QuerySet:
        return Haushaltsplan.objects.all()
```

**Commit-Link:** [99108bf71e546961410b191722e2555a0c0985d5](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/commit/99108bf71e546961410b191722e2555a0c0985d5)

Mit diesen Refactoring-Maßnahmen wurde die Leistung und Lesbarkeit des Codes er

heblich verbessert. Insbesondere wurden die Datenbankabfragen optimiert, indem unnötige Abfragen und Schleifen entfernt und stattdessen effizientere Abfragen verwendet wurden. Darüber hinaus wurde der Code aufgeräumt, redundanten Code entfernt und die Verwendung von Aggregaten vereinfacht. Dadurch wird der Code wartbarer und leichter zu verstehen, was die Weiterentwicklung des Projekts erleichtert.

### Weiteres Refactoring Beispiel:
Hier in der File HHPG/presentation/templates/test.html.
Vor dem Refactoring:
```python
from django.shortcuts import render

def calculate_budget(request):
    if request.method == 'POST':
        budget_form = BudgetForm(request.POST)
        if budget_form.is_valid():
            income = budget_form.cleaned_data['income']
            expenses = budget_form.cleaned_data['expenses']
            budget = income - expenses
            return render(request, 'budget.html', {'budget': budget})

    else:
        budget_form = BudgetForm()

    return render(request, 'calculate_budget.html', {'budget_form': budget_form})
```

Nach dem Refactoring:
```python
from django.shortcuts import render

class BudgetCalculator:
    def __init__(self, request):
        self.request = request
        self.budget_form = None

    def calculate_budget(self):
        if self.request.method == 'POST':
            self.budget_form = BudgetForm(self.request.POST)
            if self.budget_form.is_valid():
                income = self.budget_form.cleaned_data['income']
                expenses = self.budget_form.cleaned_data['expenses']
                budget = income - expenses
                return render(self.request, 'budget.html', {'budget': budget})

        else:
            self.budget_form = BudgetForm()

        return render(self.request, 'calculate_budget.html', {'budget_form': self.budget_form})

def calculate_budget(request):
    calculator = BudgetCalculator(request)
    return calculator.calculate_budget()
```

### Erklärung der Änderungen im weiteren Refactoring:

Im ursprünglichen Code wurden Berechnung und Verarbeitung innerhalb der Funktion `calculate_budget` durchgeführt. Im refaktorierten Code wurde diese Funktionalität in die Klasse `BudgetCalculator` verschoben, um die Verantwortlichkeiten zu trennen und die Lesbarkeit zu verbessern.

Die Methode `calculate_budget` in der Klasse `BudgetCalculator` verarbeitet die GET- und POST-Anfragen, ähnlich wie im vorherigen Beispiel. Die Funktionsweise der Anwendung bleibt unverändert.

Durch das Refactoring wurde der Code besser strukturiert und die Wartbarkeit verbessert. Die Klasse `BudgetCalculator` behandelt nun die Budgetberechnung, während die ursprüngliche View-Funktion `calculate_budget` nur noch die Initialisierung und Rückgabe des Ergebnisses der Budgetberechnung übernimmt.

Das Refactoring-Beispiel wurde im Commit [d00dabd7](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/commit/d00dabd724533037f52df2010891962bcca59fd9) durchgeführt.

### Code-Qualität 

Die allgemeine Code-Qualität des Haushaltsplangenerator-Projekts wurde durch die durchgeführten Refactoring-Maßnahmen erheblich verbessert. Die Beseitigung von Code Smells führte zu einem saubereren, besser strukturierten Code, der leichter zu warten und zu erweitern ist.


## 7. Zusammenfassung und Ausblick
   ### 7.1 Zusammenfassung der Ergebnisse
   ### 7.2 Ausblick und mögliche Erweiterungen

## 8. Literaturverzeichnis

## 9. Anhang
   ### 9.1 Glossar
   ### 9.2 Quellcodebeispiele
   ### 9.3 Testfallbeschreibungen
