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
   ### 2.1 Domain Driven Design (Verwendung begründen)
   ### 2.2 Clean Architecture (Verwendung begründen)
   ### 2.3 Programming Principles (Verwendung begründen)

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
