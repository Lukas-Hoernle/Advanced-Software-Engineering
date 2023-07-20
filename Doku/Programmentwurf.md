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
[//]: # (Etwas konkretere Beispiele in 5)

### 5.1 Umsetzung der Schichtenarchitektur

Die zuvor geplante Schichtenarchitektur (siehe Kapitel 4.2.1) wurde während der Implementierung praktisch umgesetzt. Jede Schicht wurde klar voneinander getrennt, um die Verantwortlichkeiten zu isolieren und die Wartbarkeit der Software zu verbessern.

#### Interaktion der Schichten

Die Schichten interagieren miteinander über klar definierte Schnittstellen. Ein Beispiel hierfür ist die Datei "HHPG/domain/repository/aufwand_repository.py" Die Präsentationsschicht kommuniziert mit der Anwendungsschicht, indem sie die Anwendungslogik aufruft, um Aktionen des Benutzers zu verarbeiten. Die Anwendungsschicht greift wiederum auf die Domain-Schicht zu, um die Geschäftslogik und -regeln umzusetzen. Die Domain-Schicht enthält die Entities und Repositories des Haushaltsplangenerators. Die Infrastruktur-Schicht kümmert sich um technische Details wie Datenbankanbindung und externe Datenquellen.

Durch diese klare Trennung der Verantwortlichkeiten ist die Architektur gut strukturiert und erleichtert die Wartbarkeit und Erweiterbarkeit des Haushaltsplangenerators.

#### Vorteile und Herausforderungen der Schichtenarchitektur

Die Schichtenarchitektur bietet mehrere Vorteile während der Implementierung. Die klare Trennung der Verantwortlichkeiten ermöglicht es, einzelne Schichten unabhängig voneinander zu entwickeln und zu testen. Dadurch wird der Code besser strukturiert und leichter verständlich. Änderungen in einer Schicht haben weniger Auswirkungen auf andere Schichten, was die Wartbarkeit erhöht.

Die Herausforderungen der Schichtenarchitektur bestehen darin, die Kommunikation zwischen den Schichten effizient zu gestalten. Der Overhead durch die Verwendung von Schnittstellen kann in manchen Fällen die Leistung beeinträchtigen. Es ist wichtig, die Schnittstellen sorgfältig zu gestalten, um die Performance zu optimieren. Beispiele hierfür können in der Infrastruktur-schicht des Projektes gefunden werden. 

### 5.2 Implementierung der Domain-Logik

Die Domain-Logik des Haushaltsplangenerators wurde detailliert umgesetzt. Die Entities repräsentieren die Hauptobjekte des Systems wie Haushaltspläne, Haushaltsposten und Projekte. Repositories bieten eine Schnittstelle zur Datenbank und ermöglichen den Zugriff auf die Entities.

Die Geschäftsregeln und -logik wurden in den entsprechenden Klassen der Domain-Schicht umgesetzt. 

Die saubere Trennung zwischen der Domain-Schicht und anderen Schichten erleichterte das Testen der Geschäftslogik und trug zur Entkopplung des Codes bei.
 
### 5.3 Unit Testing

Unit Tests wurden als zentrales Element für die Qualitätssicherung und Fehlererkennung in der Software eingesetzt. Für jede Schicht wurden separate Tests geschrieben, um sicherzustellen, dass die einzelnen Komponenten korrekt funktionieren.

Die Unit Tests deckten verschiedene Testfälle ab, einschließlich positiver und negativer Szenarien. Sie halfen dabei, Fehler frühzeitig zu erkennen und die Softwarequalität zu verbessern.

Der Einsatz von Unit Tests hatte einen positiven Einfluss auf die Gesamtqualität des Projekts, da die Entwickler mehr Vertrauen in den Code hatten und Änderungen mit größerer Sicherheit vornehmen konnten. Obwohl das Schreiben von Unit Tests zusätzlichen Aufwand erforderte, zahlte es sich durch die Reduzierung von Fehlern und die einfachere Wartung langfristig aus.

Die Implementierung von Unit Tests hat jedoch auch die Entwicklungszeit etwas verlängert. Es war wichtig, einen angemessenen Aufwand für die Testabdeckung festzulegen, um den richtigen Kompromiss zwischen Qualitätssicherung und Entwicklungseffizienz zu finden.
Tests können im Folder HHPG/test gefunden werden. 

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
