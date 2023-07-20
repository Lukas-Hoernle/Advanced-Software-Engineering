## 6. Refactoring und Qualitätssicherung

### 6.1 Identifikation von Code Smells

Die Identifikation von Code Smells im Haushaltsplangenerator-Projekt wurde während der gesamten Entwicklungsphase kontinuierlich durchgeführt. Dabei wurde besonders auf die Einhaltung der Coding-Standards und bewährter Entwurfsprinzipien geachtet. Zudem wurden statische Code-Analysewerkzeuge verwendet, um potenzielle Probleme zu erkennen.

Die gängigsten Code Smells, die während der Entwicklung aufgedeckt wurden, waren:

1. Lange Methoden: Einige Methoden waren zu umfangreich und enthielten zu viele Verantwortlichkeiten, was die Lesbarkeit erschwerte und die Wartbarkeit beeinträchtigte.
2. Hohe Komplexität: Bestimmte Codeabschnitte wiesen eine hohe zyklomatische Komplexität auf, was die Verständlichkeit erschwerte und die Anfälligkeit für Fehler erhöhte.
3. Doppelte Codierung: Wiederholter Code führte zu einer Redundanz und erschwerte das spätere Refactoring und die Wartung des Codes.
4. Unklare Benennung: Ungenau benannte Variablen, Funktionen oder Klassen machten den Code schwer zu verstehen und führten zu Verwirrung.

Diese Code Smells hatten negative Auswirkungen auf die Codequalität und die Wartbarkeit der Software. Die Lesbarkeit des Codes wurde beeinträchtigt, was zu längeren Entwicklungszeiten und erhöhtem Zeitaufwand für Fehlerbehebungen führte. Zudem wurde die Erweiterbarkeit des Systems erschwert, da sich Änderungen an unklarem oder doppeltem Code auf mehrere Stellen im Code auswirken konnten.

### 6.2 Durchführung von Refactoring-Maßnahmen

Um die Code Smells zu beseitigen und die Codequalität zu verbessern, wurden umfangreiche Refactoring-Maßnahmen durchgeführt. Dabei wurden die folgenden Schritte unternommen:

1. Aufteilung langer Methoden: Lange Methoden wurden in kleinere, besser lesbare Methoden unterteilt. Dadurch wurden die Verantwortlichkeiten klarer strukturiert und die Lesbarkeit erhöht.
2. Reduzierung der Komplexität: Komplexe Codeabschnitte wurden überarbeitet und in einfachere, besser verständliche Strukturen umgewandelt. Dies reduzierte die Anfälligkeit für Fehler und erleichterte das Verständnis des Codes.
3. Eliminierung doppelter Codierung: Doppelter Code wurde in separate Funktionen oder Klassen extrahiert und an einer zentralen Stelle zusammengeführt. Dadurch wurde die Wartbarkeit erhöht und Redundanzen wurden vermieden.
4. Verbesserung der Benennung: Variablen, Funktionen und Klassen wurden präziser benannt, um ihre Funktion und Bedeutung klarer zu kommunizieren.

### 6.3 Begründung der angewendeten Refactorings
[//]: # (Begründung des spezifischen Refactorings)

Die Refactoring-Maßnahmen wurden gezielt durchgeführt, um kritische Code Smells zu beheben, die die Codequalität und Wartbarkeit beeinträchtigten. Längere Methoden wurden aufgeteilt, hohe Komplexität reduziert, und doppelter Code wurde eliminiert.

Die positiven Auswirkungen waren:
- Verbesserte Lesbarkeit und Verständlichkeit des Codes.
- Geringeres Fehlerpotenzial und robustere Codebasis.
- Erhöhte Wartbarkeit und leichtere Weiterentwicklung.
- Beschleunigte Entwicklung durch effizientere Arbeitsabläufe.

Die Refactorings führten zu einer nachhaltigen und skalierbaren Software mit besserer Codequalität und Wartbarkeit. Code Reviews und gute Entwurfsprinzipien unterstützten den Prozess der Codepflege und -verbesserung.
Die positiven Auswirkungen waren:
- Verbesserte Lesbarkeit und Verständlichkeit des Codes.
- Geringeres Fehlerpotenzial und robustere Codebasis.
- Erhöhte Wartbarkeit und leichtere Weiterentwicklung.
- Beschleunigte Entwicklung durch effizientere Arbeitsabläufe.

Die Refactorings führten zu einer nachhaltigen und skalierbaren Software mit besserer Codequalität und Wartbarkeit. Code Reviews und gute Entwurfsprinzipien unterstützten den Prozess der Codepflege und -verbesserung.

### 6.4 Code-Qualität und Code Reviews

Die allgemeine Code-Qualität des Haushaltsplangenerator-Projekts wurde durch die durchgeführten Refactoring-Maßnahmen erheblich verbessert. Die Beseitigung von Code Smells führte zu einem saubereren, besser strukturierten Code, der leichter zu warten und zu erweitern ist.

Während des Refactoring und der Qualitätssicherung traten auch Herausforderungen auf. Die Anpassung bestehender Funktionen und Tests an die neuen Strukturen kann zeitaufwändig sein und erfordert eine sorgfältige Planung. Es war wichtig, die Auswirkungen von Refactorings auf andere Teile des Codes zu berücksichtigen und sicherzustellen, dass keine Funktionalität beeinträchtigt wurde. Dennoch haben diese Bemühungen dazu beigetragen, die langfristige Qualität und Wartbarkeit des Haushaltsplangenerators zu gewährleisten.

## 7. Zusammenfassung und Ausblick
   ### 7.1 Zusammenfassung der Ergebnisse
   ### 7.2 Ausblick und mögliche Erweiterungen

## 8. Literaturverzeichnis

## 9. Anhang
   ### 9.1 Glossar
   ### 9.2 Quellcodebeispiele
   ### 9.3 Testfallbeschreibungen
