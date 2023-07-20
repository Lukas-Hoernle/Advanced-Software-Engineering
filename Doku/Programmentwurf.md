# Inhaltsverzeichnis

## 1. Einleitung
   - 1.1 Motivation

Die vorliegende Arbeit fokussiert sich auf die Entwicklung eines Prototyps für den "Haushaltsplangenerator", der im Rahmen der Vorlesung "Advanced Software Engineering" entstanden ist. Die Idee für den Haushaltsplan entstand aus der Notwendigkeit, als "Finanzer der Studierendenvertretung" innerhalb der Dualen Hochschule Baden-Württemberg regelmäßig Haushaltspläne zu erstellen und dem Studierendenparlament vorzustellen.

Während meiner ehrenamtlichen Tätigkeit als "Finanzer" innerhalb der Studierendenvertretung Karlsruhe wurde mir bewusst, dass die bisherige Praxis der Haushaltsplanung mit Hilfe von Excel-Tabellen ineffizient und zeitaufwändig ist. Die Verwaltung und Analyse komplexer finanzieller Informationen gestaltete sich in einer unübersichtlichen Tabellenkalkulation als mühsam und fehleranfällig.

Vor diesem Hintergrund entstand die Idee, einen speziellen "Haushaltsplangenerator" zu entwickeln, der die Haushaltsplanung optimiert und menschliche Fehlerquellen minimiert. Das Projekt wurde als Prototyp im Rahmen der Vorlesung "Advanced Software Engineering" umgesetzt.

Der Schwerpunkt lag dabei auf der Implementierung eines effizienten Backends, da die Funktionalität und Datenverarbeitung in dieser Komponente einen entscheidenden Einfluss auf die Effizienz und Genauigkeit der Haushaltsplanung haben. Als Ziel wurde eine angenehme und benutzerfreundliche Webanwendung konzipiert, um den gesamten Prozess der Haushaltsplanung zu vereinfachen und zu optimieren.

Dieser Prototyp dient nicht nur als Lösung für meine persönliche Herausforderung als "Finanzer", sondern auch als Proof-of-Concept, der anderen Studierendenvertretungen oder ähnlichen Organisationen als Modell dienen kann. Im Rahmen des Projekts wurden die erlernten Konzepte und Prinzipien der Programmierung sowie der Einsatz von Unit Tests in einem realen Anwendungskontext verifiziert und angewendet.

Abschließend wird der angestrebte Prototyp des "Haushaltsplangenerators" als Grundlage für zukünftige Entwicklungen und Verfeinerungen festgelegt. Die Umsetzung eines strukturierten, flexiblen und effizienten Haushaltsplanungssystems wird nicht nur meine Arbeitsabläufe optimieren, sondern auch die Effektivität und Transparenz der finanziellen Ressourcenverwaltung in der Studierendenvertretung erheblich verbessern.

  - 1.2 Tech Stack

Aufgrund der aktuellen Zeitprobleme, die durch die anstehende Klausurphase und das Nachholen von Klausuren aufgrund eines Armbruchs entstanden sind, musste für die Entwicklung des "Haushaltsplangenerators" ein effizienter und zeitsparender Techstack gewählt werden. Gleichzeitig befand ich mich in der Endphase meiner Bachelorarbeit, was die Zeitressourcen zusätzlich einschränkte. Dennoch wollte ich die Gelegenheit nutzen, um neue Techniken und Frameworks auszuprobieren, um meinen Horizont zu erweitern.

Die Wahl des Techstacks fiel letztendlich auf Django, ein Python-Framework, das mir von meinem Kommilitonen Marc Gökce empfohlen wurde. Die Entscheidung für Django war motiviert durch dessen Popularität, aktive Community und den Ruf als leistungsfähiges Framework für die Entwicklung von Webanwendungen. Durch die Unterstützung von Django sollte es möglich sein, schnell eine funktionale Webanwendung aufzubauen und den Entwicklungsprozess zu beschleunigen.

Jedoch stieß ich während der Entwicklung auf einen Nachteil von Django, der nicht zu unterschätzen war. Django ist darauf ausgelegt, effizient zu arbeiten und wenig Codezeilen zu produzieren. Da das Projekt jedoch eine Mindestzahl an Codezeilen erforderte, führte dies zu einer unerwünschten Situation, in der unnötiger Code entstand, der lediglich als Mittel zum Zweck diente, um die Anforderung an Codezeilen zu erfüllen. Dies führte zu einem nicht unerheblichen Umfang an Code, der nicht immer der sauberen Architektur entsprach.

Trotz dieser Herausforderung ermöglichte der gewählte Techstack mit Django dennoch eine schnelle Prototypenentwicklung, wodurch der Fokus auf die Implementierung der Kernfunktionen des Haushaltsplangenerators gelegt werden konnte. In Anbetracht der zeitlichen Restriktionen und der Tatsache, dass der Prototyp als Proof-of-Concept diente, wurde die Entscheidung für Django als technologische Basis dennoch als geeignete Kompromisslösung angesehen.

Abschließend wird der angestrebte Prototyp des "Haushaltsplangenerators" als grundlegende Grundlage für zukünftige Entwicklungen und Verfeinerungen festgelegt. Die Umsetzung eines strukturierten, flexiblen und effizienten Haushaltsplanungssystems wird nicht nur meine Arbeitsabläufe optimieren, sondern auch die Effektivität und Transparenz der finanziellen Ressourcenverwaltung in der Studierendenvertretung erheblich verbessern.

   - 1.3 Zielsetzung
   - 1.4 Aufbau der Arbeit

## 2. Theoretische Grundlagen
   - 2.1 Domain Driven Design (Verwendung begründen)
   - 2.2 Clean Architecture (Verwendung begründen)
   - 2.3 Programming Principles (Verwendung begründen)

## 3. Motivation und Einleitung zum Praxisprojekt: Haushaltsplangenerator
   - 3.1 Beschreibung des Projektkontexts
   - 3.2 Integration der erlernten Konzepte und Prinzipien
   - 3.3 Herausforderungen und Lösungsansätze

## 4. Analyse und Design
   - 4.1 Anforderungsanalyse
   - 4.2 Architekturdesign
      - 4.2.1 Schichtarchitekturplanung und Begründung
      - 4.2.2 Entwurf der Domain-Schicht
      - 4.2.3 Entwurf der Infrastruktur-Schicht
   - 4.3 Design Patterns
      - 4.3.1 Observer Pattern (Einsatz und Begründung)
      - 4.3.2 Factory Pattern (Einsatz und Begründung)

## 5. Implementierung
   - 5.1 Umsetzung der Schichtenarchitektur
   - 5.2 Implementierung der Domain-Logik
   - 5.3 Einbindung von externen Datenquellen
   - 5.4 Unit Testing (Einsatz und Begründung von Unit Tests und Mocks)

## 6. Refactoring und Qualitätssicherung
   - 6.1 Identifikation von Code Smells
   - 6.2 Durchführung von Refactoring-Maßnahmen
   - 6.3 Begründung der angewendeten Refactorings
   - 6.4 Code-Qualität und Code Reviews

## 7. Zusammenfassung und Ausblick
   - 7.1 Zusammenfassung der Ergebnisse
   - 7.2 Ausblick und mögliche Erweiterungen

## 8. Literaturverzeichnis

## 9. Anhang
   - 9.1 Glossar
   - 9.2 Quellcodebeispiele
   - 9.3 Testfallbeschreibungen
