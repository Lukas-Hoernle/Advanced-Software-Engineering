## 3. Motivation und Einleitung zum Praxisprojekt: Haushaltsplangenerator

### 3.1 Beschreibung des Projektkontexts

Der "Haushaltsplangenerator" ist ein Praxisprojekt, das entwickelt wurde, um eine leistungsfähige und anwenderfreundliche Softwarelösung zu schaffen. Ziel ist es, Organisationen und Gremien in der DHBW bei der effizienten Erstellung und Verwaltung von Haushaltsplänen zu unterstützen. Die Verwaltung von Haushaltsplänen ist oft eine komplexe Aufgabe, die sorgfältige Planung und Berücksichtigung verschiedener Gremien und Projekte erfordert.

Die Aufgabenstellung des Projekts besteht primär darin, ein Backend zu entwickeln, das es ermöglicht, Haushaltspläne zu generieren und eine Alternative zu Excel zu bieten. Zusätzlich wurde eine bedienbare Benutzeroberfläche entwickelt, die es den Benutzern ermöglicht, Haushaltspläne zu erstellen und Projekte zu verwalten. Die Oberfläche war zwar nicht der Fokus des Projekts, dennoch benötigte sie Zeit, um funktionsfähig zu sein. Als Lösungsansatz wurde ein Kompromiss aus User Experience und Entwicklungsaufwand gewählt.

Die Zielgruppe des "Haushaltsplangenerator" umfasst Gremien der DHBW. Im aktuellen Prototypen ist er lediglich für Studierendenvertretungen der verschiedenen Standorte geeignet. Das Projekt kann allerdings für weitere Gremien sowie überregionale Arbeitskreise erweitert werden.

### 3.2 Integration der erlernten Konzepte und Prinzipien

Im "Haushaltsplangenerator" wurden verschiedene erlernte Konzepte und Prinzipien angewendet, um die Softwarearchitektur und Codequalität zu verbessern.

Die Clean Architecture wurde verwendet, um eine übersichtliche und gut strukturierte Softwarearchitektur zu erreichen. Durch die klare Trennung der Verantwortlichkeiten in verschiedene Layer ist der "Haushaltsplangenerator" leicht erweiterbar und wartbar. Dies ermöglichte es, neue Funktionen hinzuzufügen und bestehende Funktionen anzupassen, ohne dabei unbeabsichtigt andere Teile der Anwendung zu beeinflussen.

Die SOLID-Prinzipien (Single Responsibility Principle, Open/Closed Principle, Liskov Substitution Principle, Interface Segregation Principle und Dependency Inversion Principle) und die GRASP-Prinzipien (General Responsibility Assignment Software Patterns) wurden ebenfalls angewendet, um eine saubere und gut strukturierte Codebasis zu schaffen. Diese Prinzipien unterstützten die Trennung der Verantwortlichkeiten und reduzierten die Kopplung zwischen den Klassen.

Domain Driven Design (DDD) wurde berücksichtigt, um eine klare Trennung zwischen Geschäftslogik und technischen Details zu erreichen. Die Strukturierung in Domänen-übergreifende Bounded Contexts sorgte für eine übersichtliche Organisation des Projekts und eine erhöhte Wartbarkeit.

### 3.3 Herausforderungen und Lösungsansätze

Während der Entwicklung des Haushaltsplangenerators traten verschiedene Herausforderungen auf, die erfolgreich bewältigt wurden.

1. Zeitprobleme: Die Umsetzung des Projekts erforderte eine intensive Einzelarbeit, da keine Teammitglieder zur Verfügung standen. Gleichzeitig mussten Klausuren nachgeholt und die Bachelorarbeit bearbeitet werden. Als Lösungsansatz wurde Python und Django verwendet, da sie weniger Zeilen Code benötigen und somit Zeit eingespart wurde.

2. Unbekannte Technologien: Die Verwendung neuer Technologien im Tech-Stack stellte eine Herausforderung dar, da einige Technologien nicht vertraut waren. Um dieses Problem zu bewältigen, wurden ausgiebige Recherchen und Online-Tutorials genutzt, um das nötige Wissen aufzubauen und die Technologien erfolgreich in das Projekt zu integrieren.

3. Benutzeroberfläche: Die Benutzeroberfläche erforderte zwar nicht den Hauptfokus des Projekts, dennoch benötigte sie Zeit, um funktionsfähig zu sein. Als Lösungsansatz wurde ein Kompromiss aus User Experience und Entwicklungsaufwand gewählt, um eine akzeptable Benutzererfahrung zu gewährleisten ohne zu große Konsequenzen im Backend zu erfahren.

Die Lösungsansätze und deren Ergebnisse wurden reflektiert, und es wurde festgestellt, dass die Anwendung der Konzepte und Prinzipien wesentlich zur Verbesserung der Softwarearchitektur und Codequalität beigetragen hat. Die klare Trennung der Verantwortlichkeiten und die flexible Schichtenarchitektur ermöglichten es, neue Funktionen hinzuzufügen und Änderungen vorzunehmen, ohne den bestehenden Code zu beeinträchtigen. Dies erhöhte die Wartbarkeit und Skalierbarkeit der Anwendung und trug dazu bei, dass die Software den Anforderungen der Benutzer gerecht wird.

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
