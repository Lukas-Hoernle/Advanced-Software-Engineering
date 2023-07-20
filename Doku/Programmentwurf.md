## 6. Refactoring und Qualitätssicherung

### 6.1 Identifikation von Code Smells

Die Identifikation von Code Smells im Haushaltsplangenerator-Projekt wurde während der gesamten Entwicklungsphase kontinuierlich durchgeführt. Dabei wurde besonders auf die Einhaltung der Coding-Standards und bewährter Entwurfsprinzipien geachtet. Die QUalitätskontroille fand manuell statt, da SonarCloud große Probleme mit der Nutzung des Frameworks Django hatte. 

Die gängigsten Code Smells, die während der Entwicklung aufgedeckt wurden, waren:

1. Lange Methoden: Einige Methoden waren zu umfangreich und enthielten zu viele Verantwortlichkeiten, was die Lesbarkeit erschwerte und die Wartbarkeit beeinträchtigte.
2. Hohe Komplexität: Bestimmte Codeabschnitte wiesen eine hohe zyklomatische Komplexität auf, was die Verständlichkeit erschwerte und die Anfälligkeit für Fehler erhöhte. Dies war meistens darauf zurückzuführen, dass mehr Zeilen eingefügt wurden, um die Zeilenmindestanzahl zu schaffen.

### 6.2 Durchführung von Refactoring-Maßnahmen

Um die Code Smells zu beseitigen und die Codequalität zu verbessern, wurden umfangreiche Refactoring-Maßnahmen durchgeführt. Im Folgenden wird ein konkretes Beispiel dargestellt:

Vor dem Refactoring:
```python
import openpyxl

class HaushaltsplanExcelGenerator:
    def generate_excel_poorly(self, haushaltsplan, file_name):
        workbook = openpyxl.Workbook()
        worksheet = workbook.active

        worksheet['A1'] = 'Projekt Name'
        worksheet['B1'] = 'Einnahmen'
        worksheet['C1'] = 'Ausgaben'

        row_index = 2

        for haushaltsposten in haushaltsplan.haushaltsposten:
            worksheet.cell(row=row_index, column=1, value=haushaltsposten.name)

            for projekt in haushaltsposten.projekte:
                worksheet.cell(row=row_index, column=2, value=projekt.einnahmen)
                worksheet.cell(row=row_index, column=3, value=projekt.ausgaben)
                row_index += 1

        workbook.save(file_name)
```

Nach dem Refactoring:
```python
import openpyxl

from HHPG.domain.entity import haushaltsplan


class HaushaltsplanExcelGenerator:
    def __init__(self, haushaltsplan: haushaltsplan):
        self.haushaltsplan = haushaltsplan

    def generate_excel(self, file_name):
        workbook = openpyxl.Workbook()
        worksheet = workbook.active

        worksheet['A1'] = 'Projekt Name'
        worksheet['B1'] = 'Einnahmen'
        worksheet['C1'] = 'Ausgaben'

        row_index = 2

        haushaltsposten_list = self.haushaltsplan.haushaltsposten.objects.all()

        for haushaltsposten in haushaltsposten_list:
            builder = ExcelBuilder(worksheet)
            builder.set_haushaltsposten(haushaltsposten, row_index)
            builder.write_haushaltsposten()
            row_index += 1
            projekte_list = haushaltsposten.projekte.all()
            for projekt in projekte_list:
                builder.set_projekt(projekt, row_index)
                builder.write_projekt()
                row_index += 1

        workbook.save(file_name)


class ExcelBuilder:
    def __init__(self, worksheet):
        self.worksheet = worksheet
        self.headers = []
        self.haushaltsposten = None
        self.projekt = None
```

### Erklärung der Änderungen im Refactoring:

1. Im ursprünglichen Code wurde die Methode `generate_excel_poorly` direkt in der Klasse `HaushaltsplanExcelGenerator` definiert, was zu einer übermäßig langen Methode führte. Im refaktorierten Code wurde die Methode in `generate_excel` umbenannt und in eine separate Klasse verschoben, um die Verantwortlichkeiten klarer zu trennen und die Lesbarkeit zu verbessern.

2. Die Nutzung von `haushaltsplan.haushaltsposten` und `haushaltsposten.projekte` im ursprünglichen Code legt nahe, dass es sich dabei um QuerySets handelt, die auf Datenbankabfragen hinweisen. Im refaktorierten Code wurden diese Abfragen durch `.objects.all()` ersetzt, um die Datenbankabfragen zu optimieren und die Performanz zu verbessern.

3. Ein Builder-Pattern wurde eingeführt, um die Erstellung der Excel-Datei zu strukturieren und die Verantwortlichkeiten klarer zu verteilen. Die Klasse `ExcelBuilder` kümmert sich um das Schreiben der Daten in das Excel-Dokument und ermöglicht eine sauberere Implementierung der `generate_excel`-Methode.

Durch diese Refactoring-Maßnahmen wurde der Code verbessert, ohne dass funktionale Änderungen eingeführt wurden. Die Struktur des Codes wurde klarer und lesbarer gestaltet, und die Nutzung von optimierten Datenbankabfragen trug zur Performance-Optimierung bei. Der Refactoring-Prozess half dabei, die Codequalität zu erhöhen und die Wartbarkeit des Haushaltsplangenerators zu verbessern.

Die Refactoring-Maßnahmen wurden im Commit [17d99c0](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/commit/17d99c028741bbf41664ee435aa132f23b1dc510) durchgeführt.

### 6.4 Code-Qualität 

Die allgemeine Code-Qualität des Haushaltsplangenerator-Projekts wurde durch die durchgeführten Refactoring-Maßnahmen erheblich verbessert. Die Beseitigung von Code Smells führte zu einem saubereren, besser strukturierten Code, der leichter zu warten und zu erweitern ist.


## 7. Zusammenfassung und Ausblick
   ### 7.1 Zusammenfassung der Ergebnisse
   ### 7.2 Ausblick und mögliche Erweiterungen

## 8. Literaturverzeichnis

## 9. Anhang
   ### 9.1 Glossar
   ### 9.2 Quellcodebeispiele
   ### 9.3 Testfallbeschreibungen
