
## 3. Motivation und Einleitung zum Praxisprojekt: Haushaltsplangenerator

### 3.1 Beschreibung des Projektkontexts

Der "Haushaltsplangenerator" ist ein Praxisprojekt, das entwickelt wurde, um eine leistungsfähige und anwenderfreundliche Softwarelösung zu schaffen. Ziel ist es, Organisationen und Gremien in der DHBW bei der effizienten Erstellung und Verwaltung von Haushaltsplänen zu unterstützen. Die Verwaltung von Haushaltsplänen ist oft eine komplexe Aufgabe, die sorgfältige Planung und Berücksichtigung verschiedener Gremien und Projekte erfordert.

Die Aufgabenstellung des Projektsprimär darin ein Backend zu entwickelln, das es ermöglicht diese zu generieren und eine Alternative zu Excel bietet. Zusätzlich wurde eine bedienbare Benutzeroberfläche entwickelt, die es den Benutzern ermöglicht, Haushaltspläne zu erstellen und Projekte zu verwalten. Die Oberfläche ist jedoch noch ausbaufähig, da es sich beim umschriebenen Projekt um einen Prototypen handelt. 

Die Zielgruppe des "Haushaltsplangenerators" umfasst Gremien der DHBW. Im akt uellen Prototypen ist er lediglich für Studierendenvertretungen der verschiedenen Standorte geeignet. Das Projekt kann allerdings für weitere Gremien sowie überregionale Arbeitskreise erweitert werden. 

### 3.2 Integration der erlernten Konzepte und Prinzipien

In der Umsetzung des "Haushaltsplangenerators" wurden verschiedene theoretische Konzepte und Prinzipien integriert, um die Softwarearchitektur und Codequalität zu verbessern.

Domain Driven Design (DDD) wurde angewendet, um eine klare Trennung zwischen Geschäftslogik und technischen Details zu erreichen. Die Strukturierung in Domänen-übergreifende Bounded Contexts sorgte für eine übersichtliche Organisation des Projekts und eine erhöhte Wartbarkeit.

Die Anwendung der Clean Architecture führte zur Schaffung einer flexiblen Schichtenarchitektur, in der Geschäftslogik, Schnittstellen und Datenbankzugriffe klar voneinander getrennt sind. Dadurch wurden die Abhängigkeiten minimiert und die Austauschbarkeit der Technologien verbessert.

Die Berücksichtigung der SOLID-Prinzipien (Single Responsibility Principle, Open/Closed Principle, Liskov Substitution Principle, Interface Segregation Principle und Dependency Inversion Principle) führte zu einem gut strukturierten und wartbaren Code. Die Prinzipien unterstützten die Trennung der Verantwortlichkeiten und reduzierten die Kopplung zwischen den Klassen.

Ebenso wurden die GRASP-Prinzipien (General Responsibility Assignment Software Patterns) angewendet, um klare Verantwortlichkeiten für die einzelnen Klassen zu definieren und eine hohe Kohäsion zu erreichen.

### 3.3 Herausforderungen und Lösungsansätze

Während der Entwicklung des Haushaltsplangenerators traten verschiedene Herausforderungen auf, die erfolgreich bewältigt wurden.

Eine Herausforderung bestand in der Modellierung der komplexen Budgetierungs- und Ressourcenplanungsprozesse. Durch die Anwendung von Domain Driven Design konnten die Geschäftslogik und -regeln klar definiert und auf verschiedene Bounded Contexts aufgeteilt werden, um die Komplexität zu reduzieren.

Die effiziente Verwaltung von Projekten und Ressourcen war ein weiteres Thema. Hier kam das Creator-Prinzip aus den GRASP-Prinzipien zum Einsatz, um sicherzustellen, dass die Verantwortung für die Erstellung von Objekten immer bei den entsprechenden Klassen selbst liegt. Dadurch wurde die Verwaltung von Projekten und Ressourcen erleichtert und die Abhängigkeiten zwischen den Klassen reduziert.

Die Lösungsansätze und deren Ergebnisse wurden reflektiert, und es wurde festgestellt, dass die Anwendung der Konzepte und Prinzipien wesentlich zur Verbesserung der Softwarearchitektur und Codequalität beigetragen hat. Die klare Trennung der Verantwortlichkeiten und die flexible Schichtenarchitektur ermöglichten es, neue Funktionen hinzuzufügen und Änderungen vorzunehmen, ohne den bestehenden Code zu beeinträchtigen. Dies erhöhte die Wartbarkeit und Skalierbarkeit der Anwendung und trug dazu bei, die Projektziele effektiv zu erreichen.


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
