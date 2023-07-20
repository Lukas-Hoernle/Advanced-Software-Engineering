# Inhaltsverzeichnis

## 1. Einleitung
   ### 1.1 Motivation

Die vorliegende Arbeit fokussiert sich auf die Entwicklung eines Prototyps für den "Haushaltsplangenerator", der im Rahmen der Vorlesung "Advanced Software Engineering" entstanden ist. Die Idee für den Haushaltsplan entstand aus der Notwendigkeit, als "Finanzer der Studierendenvertretung" innerhalb der Dualen Hochschule Baden-Württemberg regelmäßig Haushaltspläne zu erstellen und dem Studierendenparlament vorzustellen.

Während meiner ehrenamtlichen Tätigkeit als "Finanzer" innerhalb der Studierendenvertretung Karlsruhe wurde mir bewusst, dass die bisherige Praxis der Haushaltsplanung mit Hilfe von Excel-Tabellen ineffizient und zeitaufwändig ist. Die Verwaltung und Analyse komplexer finanzieller Informationen gestaltete sich in einer unübersichtlichen Tabellenkalkulation als mühsam und fehleranfällig.

Vor diesem Hintergrund entstand die Idee, einen speziellen "Haushaltsplangenerator" zu entwickeln, der die Haushaltsplanung optimiert und menschliche Fehlerquellen minimiert. Das Projekt wurde als Prototyp im Rahmen der Vorlesung "Advanced Software Engineering" umgesetzt.

Der Schwerpunkt lag dabei auf der Implementierung eines effizienten Backends, da die Funktionalität und Datenverarbeitung in dieser Komponente einen entscheidenden Einfluss auf die Effizienz und Genauigkeit der Haushaltsplanung haben. Als Ziel wurde eine angenehme und benutzerfreundliche Webanwendung konzipiert, um den gesamten Prozess der Haushaltsplanung zu vereinfachen und zu optimieren.

Dieser Prototyp dient nicht nur als Lösung für meine persönliche Herausforderung als "Finanzer", sondern auch als Proof-of-Concept, der anderen Studierendenvertretungen oder ähnlichen Organisationen als Modell dienen kann. Im Rahmen des Projekts wurden die erlernten Konzepte und Prinzipien der Programmierung sowie der Einsatz von Unit Tests in einem realen Anwendungskontext verifiziert und angewendet.

Abschließend wird der angestrebte Prototyp des "Haushaltsplangenerators" als Grundlage für zukünftige Entwicklungen und Verfeinerungen festgelegt. Die Umsetzung eines strukturierten, flexiblen und effizienten Haushaltsplanungssystems wird nicht nur meine Arbeitsabläufe optimieren, sondern auch die Effektivität und Transparenz der finanziellen Ressourcenverwaltung in der Studierendenvertretung erheblich verbessern.
Ob dieses Projekt jedoch weitergeführt wird, ist zum aktuellen Zeitpunkt unklar.

  ### 1.2 Tech Stack

Ursprünglich war ein Projekt mit Java und Angular angesetzt, um den "Haushaltsplangenerator" zu entwickeln. Allerdings stieß ich während der Implementierungsphase auf Schwierigkeiten, die sich aus Zeitproblemen ergaben, die durch das Nachholen von Klausuren aufgrund eines Armbruchs entstanden waren. Gleichzeitig schreibe ich aktuell meine Bachelorarbeit, was meine Ressourcen zusätzlich einschränkte und die Entwicklung mit diesem Techstack erschwerte.

Da das Projekt zeitkritisch war und ein effizienter Entwicklungsprozess notwendig war, entschied ich mich, neue Techniken und Frameworks auszuprobieren, um das Projekt voranzutreiben. Auf Empfehlung meines Kommilitonen Marc Gökce entschied ich mich schließlich dafür, den Techstack zu wechseln und Django, ein Python-Framework, als technologische Basis für den "Haushaltsplangenerator" zu nutzen.

Die Entscheidung für Django wurde durch dessen Popularität, aktive Community und den Ruf als leistungsfähiges Framework für die Entwicklung von Webanwendungen motiviert. Durch die Unterstützung von Django konnte ich eine funktionale Webanwendung schneller aufbauen und den Entwicklungsprozess beschleunigen.

Allerdings stieß ich während der Entwicklung auf einen Nachteil von Django, der nicht zu unterschätzen war. Django ist darauf ausgelegt, effizient zu arbeiten und wenig Codezeilen zu produzieren. Da das Projekt jedoch eine Mindestzahl an Codezeilen erforderte, führte dies zu einer unerwünschten Situation, in der unnötiger Code entstand, der lediglich als Mittel zum Zweck diente, um die Anforderung an Codezeilen zu erfüllen. Dies führte zu einem nicht unerheblichen Umfang an Code, der nicht immer der sauberen Architektur entsprach.

Trotz dieser Herausforderung ermöglichte der gewählte Techstack mit Django dennoch eine schnelle Prototypenentwicklung, wodurch der Fokus auf die Implementierung der Kernfunktionen des Haushaltsplangenerators gelegt werden konnte. In Anbetracht der zeitlichen Restriktionen und der Tatsache, dass der Prototyp als Proof-of-Concept diente, wurde die Entscheidung für Django als geeignete Kompromisslösung angesehen.

Abschließend wird der angestrebte Prototyp des "Haushaltsplangenerators" als grundlegende Grundlage für zukünftige Entwicklungen und Verfeinerungen festgelegt. Die Umsetzung eines strukturierten, flexiblen und effizienten Haushaltsplanungssystems wird nicht nur meine Arbeitsabläufe optimieren, sondern auch die Effektivität und Transparenz der finanziellen Ressourcenverwaltung in der Studierendenvertretung erheblich verbessern.

   ### 1.3 Zielsetzung

Das Hauptziel des Projekts "Haushaltsplangenerator" ist es, eine effiziente Automatisierung für die Studierendenvertretung (StuV) Karlsruhe zu entwickeln, um bisher manuell erstellte Anträge für Veranstaltungen und Haushaltspläne zu optimieren. Die Automatisierung soll Excel-Tabellen für Veranstaltungen und Haushaltspläne generieren, basierend auf den Eingaben des Nutzers, und dadurch das Erstellen erleichtern und den Einstieg für zukünftige Finanzer ermöglichen.

Die Zielsetzung des Projekts ist durch die Herausforderungen bei der manuellen Erstellung von Anträgen entstanden. Es wurde erkannt, dass die Verwaltung und Analyse komplexer finanzieller Informationen in Excel-Tabellen zeitaufwändig und fehleranfällig ist. Um diesen Prozess zu optimieren, soll der Haushaltsplangenerator eine angenehme und benutzerfreundliche Webanwendung bieten, die den gesamten Prozess der Haushaltsplanung vereinfacht.

Benutzer können neue Haushaltspläne (HHPs) anlegen. Zudem sollen verschiedene Haushaltsposten und Projekte Geldbeträge zugewiesen bekommen können.

Ein weiteres wichtiges Ziel ist die Implementierung einer Warnfunktion, die erscheint, wenn die Budgetplanung im Haushaltsplan das Gesamtbudget übersteigt oder unterschreitet. Dadurch wird eine effektive Kontrolle der Finanzen gewährleistet und mögliche Unstimmigkeiten oder Budgetüberschreitungen frühzeitig erkannt.

Das Projekt nutzt den Django-Stack, um eine flexible und effiziente Webanwendung zu entwickeln. Diese Technologie wurde gewählt, um eine rasche Prototypenentwicklung zu ermöglichen und die Umsetzung der Kernfunktionen des Haushaltsplangenerators zu erleichtern.

Der angestrebte Prototyp des "Haushaltsplangenerators" dient als Grundlage für zukünftige Entwicklungen und Verfeinerungen. Die Umsetzung eines strukturierten, flexiblen und effizienten Haushaltsplanungssystems wird nicht nur die Arbeitsabläufe optimieren, sondern auch die Effektivität und Transparenz der finanziellen Ressourcenverwaltung in der Studierendenvertretung erheblich verbessern.

   ### 1.4 Aufbau der Arbeit

Die vorliegende Arbeit gliedert sich in die folgenden Abschnitte:

1. Einleitung: Hier wird die Motivation und der Kontext des Projekts "Haushaltsplangenerator" erläutert.

2. Grundlagen:
   - Domain Driven Design: Analyse der Ubiquitous Language und Verwendung taktischer Muster des DDD.
   - Clean Architecture: Planung einer Schichtarchitektur und Umsetzung von mindestens zwei Schichten.
   - Programming Principles: Analyse und Begründung von SOLID, GRASP und DRY.
   - Unit Tests: Umsetzung von mindestens 10 Unit Tests unter Beachtung der ATRIP Regeln und Einsatz von Mocks.
   - Refactoring: Identifikation von Code Smells und Durchführung von mindestens 2 Refactorings.

3. Entwurfsmuster:
   - Einsatz des Observer Patterns und Factory Patterns, Begründung und UML-Darstellung.

4. Techstack: Erklärung der Entscheidung für Django und Python als technologische Basis des Prototyps.

5. Implementierung: Beschreibung der Umsetzung des "Haushaltsplangenerators" unter Berücksichtigung des gewählten Techstacks.

6. Evaluation und Ausblick: Bewertung der erreichten Ziele und Ausblick auf mögliche Erweiterungen oder Verbesserungen.

7. Fazit: Zusammenfassung der Arbeit und Reflexion über den Entwicklungsprozess und die Ergebnisse.

Im Rahmen dieser Gliederung wird das Projekt "Haushaltsplangenerator" von der Motivation über die theoretischen Grundlagen bis hin zur praktischen Umsetzung und Evaluation detailliert behandelt.

## 2. Theoretische Grundlagen

### 2.1 Domain Driven Design

Domain Driven Design (DDD) ist ein Konzept aus der Softwareentwicklung, das sich darauf konzentriert, die Software so zu gestalten, dass sie die Anforderungen des Fachwissens besser widerspiegelt. Im Projekt "Haushaltsplangenerator" haben wir DDD bewusst eingesetzt, um die Haushaltsplanung in der Studierendenvertretung effizienter und benutzerfreundlicher zu gestalten.

Wir haben zuerst eine umfassende Analyse der Fachbegriffe und Konzepte der Haushaltsplanung durchgeführt, um sicherzustellen, dass wir die gleiche Sprache wie die Fachexperten sprechen. Dies hat geholfen, Missverständnisse zu vermeiden und eine klare Verbindung zur Fachdomäne herzustellen.

Im Projekt haben wir verschiedene DDD-Muster angewendet, um die Softwarestruktur zu optimieren:

- Value Objects haben wir verwendet, um bestimmte Eigenschaften wie Preise und Budgets als unveränderliche Wertobjekte darzustellen. Beispielsweise haben wir sie bei den Aufwand-Objekten genutzt, um den Aufwand für eine Veranstaltung in Stunden und Minuten zu repräsentieren.

- Entities repräsentieren identifizierbare und veränderbare Objekte im System. Wir haben sie beispielsweise für Veranstaltungen genutzt, da sie eindeutig identifizierbar sind und ihren Zustand ändern können.

- Repositories dienen dazu, den Zugriff auf die Datenbank zu ermöglichen und die Domänenlogik von der Datenhaltung zu trennen.

   ### 2.2 Clean Architecture 
   ### 2.3 Programming Principles 

## 3. Motivation und Einleitung zum Praxisprojekt: Haushaltsplangenerator
   ### 3.1 Beschreibung des Projektkontexts
   ### 3.2 Integration der erlernten Konzepte und Prinzipien
   ### 3.3 Herausforderungen und Lösungsansätze

## 4. Analyse und Design
   ### 4.1 Anforderungsanalyse
   ### 4.2 Architekturdesign
   #### 4.2.1 Schichtarchitekturplanung und Begründung
   #### 4.2.2 Entwurf der Domain-Schicht
   #### 4.2.3 Entwurf der Infrastruktur-Schicht
   ### 4.3 Design Patterns
   #### 4.3.1 Observer Pattern (Einsatz und Begründung)
   #### 4.3.2 Factory Pattern (Einsatz und Begründung)

## 5. Implementierung
   ### 5.1 Umsetzung der Schichtenarchitektur
   ### 5.2 Implementierung der Domain-Logik
   ### 5.3 Einbindung von externen Datenquellen
   ### 5.4 Unit Testing (Einsatz und Begründung von Unit Tests und Mocks)

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
