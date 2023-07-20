
## 4. Analyse und Design

### 4.1 Anforderungsanalyse

Die Anforderungsanalyse für den Haushaltsplangenerator basiert auf den in der Anmelddung genannten Use Cases und der Projektkontextbeschreibung (Kapitel 3.1). Dabei wurden sowohl funktionale als auch nicht-funktionale Anforderungen erfasst.

Funktionale Anforderungen:
- Erstellung und Verwaltung von Haushaltsplänen
- Zuordnung von Aufwänden zu Projekten zu Haushaltsposten
- Erstellung einer Excel

Nicht-funktionale Anforderungen:
- Benutzerfreundliche Benutzeroberfläche
- Schöne Struktur der Excel
- Skalierbarkeit der Software

Die Prioritäten und Abhängigkeiten der Anforderungen wurden analysiert, um die Umsetzung der funktionalen Kernfunktionen zu priorisieren und sicherzustellen, dass die Software den Anforderungen der Zielgruppe gerecht wird.

### 4.2 Architekturdesign

Der Haushaltsplangenerator folgt einer Schichtarchitektur, um die Softwarestruktur übersichtlich zu gestalten und die Erweiterbarkeit zu erleichtern und den Anforderungen der Vorlesung zu entsprechen. 

#### 4.2.1 Schichtarchitekturplanung und Begründung

Die Schichtarchitektur besteht aus den folgenden Schichten:
1. Präsentationsschicht: Hier befindet sich die Benutzeroberfläche des Haushaltsplangenerators.
2. Anwendungsschicht: Diese Schicht enthält die Anwendungslogik und vermittelt zwischen der Präsentationsschicht und der Domain-Schicht.
3. Domain-Schicht: Dies ist der Kern der Anwendungslogik, der die Geschäftsregeln und -modelle enthält.
4. Infrastruktur-Schicht: Hier werden technische Details und die Datenbankanbindung implementiert.

Die Schichtarchitektur wurde gewählt, um die Software in gut abgegrenzte Bereiche zu strukturieren, was die Wartbarkeit und Erweiterbarkeit erleichtert. Durch die klare Trennung der Verantwortlichkeiten in den Schichten wird die Abhängigkeit zwischen den Komponenten reduziert.

#### 4.2.2 Entwurf der Domain-Schicht

Die Domain-Schicht enthält die Kernlogik des Haushaltsplangenerators, einschließlich der Definition von Entities und Repositories. Entities repräsentieren die Hauptobjekte des Systems und Repositories ermöglichen den Zugriff auf die Datenbank. Die saubere Trennung zwischen der Domain-Schicht und anderen Schichten erleichtert das Testen und die Austauschbarkeit.

#### 4.2.3 Entwurf der Infrastruktur-Schicht

In der Infrastruktur-Schicht werden technische Details und die Datenbankanbindung implementiert. Externe Frameworks und Bibliotheken werden hier integriert, um die Funktionalität des Haushaltsplangenerators zu erweitern. Die Infrastruktur-Schicht bietet eine Schnittstelle zur Persistenz der Daten und ermöglicht die Interaktion mit der Datenbank.

### 4.3 Design Patterns

Im Haushaltsplangenerator wurden verschiedene Design Patterns angewendet, um bestimmte Probleme zu lösen und die Softwarestruktur zu verbessern.

[//]: # (todo actual Auflistung)


#### 4.3.1 Observer Pattern

Das Observer Pattern wird verwendet, um die Kommunikation zwischen den Komponenten des Haushaltsplangenerators zu ermöglichen. Durch das Observer Pattern werden bestimmte Komponenten über Änderungen in anderen Komponenten informiert, ohne dass diese Komponenten direkt miteinander gekoppelt sind. Dies ermöglicht eine flexible und entkoppelte Kommunikation zwischen den verschiedenen Teilen des Systems.

#### 4.3.2 Factory Pattern
Im Haushaltsplangenerator wird das Factory Pattern verwendet, um die Erzeugung von Formularen (Forms) und Formsets zu vereinfachen und zu zentralisieren. Hierbei kommt das Abstract Factory Pattern zum Einsatz, um eine abstrakte Klasse `FormFactory` zu definieren, die Methoden zur Erstellung von verschiedenen Formularen und Formsets bereitstellt. Diese abstrakte Klasse dient als Basis für spezifische Implementierungen, wie die Klasse `DefaultFormFactory`.

In der Klasse `DefaultFormFactory` werden die abstrakten Methoden der `FormFactory` überschrieben, um konkrete Formulare und Formsets zurückzugeben. Zum Beispiel wird die Methode `create_haushaltsplan_form` überschrieben, um eine Instanz des `HaushaltsplanForm` zu erzeugen, und die Methode `create_projekt_formset` wird überschrieben, um eine Instanz des `ProjektFormSet` zurückzugeben.

Hier ist der relevante Teil des Codes, in dem das Factory Pattern angewendet wird:

```python
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

# ... Weitere Klassen ...

class HaushaltsplanView:
    def __init__(self, form_factory):
        self.form_factory = form_factory

    # ... Andere Methoden ...

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

    # ... Andere Methoden ...

```

Durch die Anwendung des Factory Patterns wird die Erstellung von Formularen und Formsets zentralisiert und die Abhängigkeiten zwischen den verschiedenen Komponenten reduziert. Dadurch wird der Code flexibler und besser wartbar. Außerdem ermöglicht das Factory Pattern die einfache Erweiterung des Systems um weitere Formulare und Formsets, indem neue Implementierungen der `FormFactory` erstellt werden, ohne den bestehenden Code ändern zu müssen.

[Link zur Klasse create_Haushaltsplan.py im GitHub-Repository](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/blob/Analyse-und-Design/HHPG/application/create_Haushaltsplan.py)

Die Verwendung dieser Design Patterns trägt dazu bei, die Codequalität zu verbessern und die Wartbarkeit des Haushaltsplangenerators zu erhöhen.

## 5. Implementierung
   ### 5.1 Umsetzung der Schichtenarchitektur
   ### 5.2 Implementierung der Domain-Logik
   ### 5.3 Einbindung von externen Datenquellen
   ### 5.4 Unit Testing (Einsatz und Begründung von Unit Tests und Mocks)

## 6. Refactoring und Qualitätssicherung
   ### 6.1 Identifikation von Code Smells
   ### 6.2 Durchführung von Refactoring-Maßnahmen
   ### 6.3 Begründung der angewendeten Refactorings
   ### 6.4 Code-Qualität und Code Reviews

## 7. Zusammenfassung und Ausblick
   ### 7.1 Zusammenfassung der Ergebnisse
   ### 7.2 Ausblick und mögliche Erweiterungen

## 8. Literaturverzeichnis

## 9. Anhang
   ### 9.1 Glossar
   ### 9.2 Quellcodebeispiele
   ### 9.3 Testfallbeschreibungen
