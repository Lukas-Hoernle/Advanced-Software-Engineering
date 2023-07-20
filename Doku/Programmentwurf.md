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

Im Projekt "Haushaltsplangenerator" wurde die Softwarearchitektur nach dem Prinzip der Clean Architecture strukturiert, um eine klare Trennung der Verantwortlichkeiten und eine hohe Flexibilität der Software zu erreichen. Die Clean Architecture besteht aus verschiedenen Layern, die jeweils spezifische Aufgaben und Abhängigkeiten haben.

1. **Application Layer:**
   Der Application Layer stellt die oberste Schicht der Clean Architecture dar und dient als Schnittstelle zur Kommunikation mit der Außenwelt. Hier werden die Benutzereingaben verarbeitet und die Anwendungsfälle umgesetzt. Der Application Layer kommuniziert mit dem Domain Layer, um die entsprechenden Geschäftsregeln auszuführen. (Application Layer: [Link](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/tree/master/HHPG/application))

2. **Domain Layer:**
   Der Domain Layer bildet das Herzstück der Clean Architecture und enthält die Kernlogik der Anwendung. Hier werden die Business-Entities und Value Objects definiert, die das Domänenwissen abbilden. Der Domain Layer ist unabhängig von den anderen Layern und enthält keine Abhängigkeiten zu Frameworks oder Datenbanken. Die Entities und Repositories sind im [domain-Ordner](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/tree/master/HHPG/domain) des Projekts strukturiert. Die Entities befinden sich im [entity-Ordner](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/tree/master/HHPG/domain/entity) und die Repositories im [repository-Ordner](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/tree/master/HHPG/domain/repository).

3. **Infrastructure Layer:**
   Der Infrastruktur-Layer enthält Implementierungsdetails, die den äußeren Rahmen der Anwendung bilden. Hier werden Datenbankzugriffe, externe Schnittstellen und Framework-spezifische Komponenten behandelt. Der Infrastruktur-Layer kommuniziert mit dem Application Layer und ermöglicht die Persistenz und Datenverwaltung. Die Implementierungen des Infrastruktur-Layers sind im [infrastruktur-Ordner](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/tree/master/HHPG/infrastruktur) des Projekts zu finden.

4. **Migration-Layer:**
   Der Migration-Layer enthält Datenbankmigrationen, die für die Erstellung und Verwaltung der Datenbankstruktur notwendig sind. Dieser Layer ermöglicht die einfache Aktualisierung der Datenbankstruktur, wenn sich das Datenmodell ändert. Die Migrationen befinden sich im [migrations-Ordner](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/tree/master/HHPG/migrations) des Projekts.

5. **Presentation Layer:**
   Der Presentation Layer ist für die Darstellung der Benutzeroberfläche verantwortlich. Hier werden die grafischen Elemente und Interaktionen mit dem Benutzer implementiert. Der Presentation Layer des Projekts befindet sich im [presentation-Ordner](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/tree/master/HHPG/presentation).

6. **Tests:**
   Die Tests haben einen eigenen Ordner im Projekt erhalten, um die Testfälle und Testabdeckung strukturiert zu organisieren. Der [test-Ordner](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/tree/master/HHPG/test) enthält alle Unit-Tests und Integrationstests, die sicherstellen, dass die Funktionalität der Anwendung korrekt und fehlerfrei ist.

Die Clean Architecture ermöglicht eine klare und flexible Strukturierung des Projekts, die eine einfache Wartung und Erweiterbarkeit der Software gewährleistet. Der Mehraufwand bei der Einführung der Clean Architecture war anfangs spürbar, jedoch legte sie eine solide Basis für zukünftige Entwicklungen und Erweiterungen. Besonders bei größeren Softwareprojekten bietet die Clean Architecture den Vorteil einer besseren Skalierbarkeit und Wartbarkeit. Die klare Trennung der Verantwortlichkeiten in den verschiedenen Layern minimiert die Abhängigkeit von externen Frameworks und ermöglicht eine unabhängige Domänenlogik. 

### 2.3 Programming Principles
In der Entwicklung des "Haushaltsplangenerators" wurden verschiedene grundlegende Programmierprinzipien angewendet, um eine saubere, wartbare und erweiterbare Codebasis zu gewährleisten. Diese Prinzipien sind bewährte Richtlinien, die helfen, qualitativ hochwertigen Code zu schreiben und Softwareprobleme effizient zu lösen.


#### SOLID-Prinzipien

Die SOLID-Prinzipien sind eine Gruppe von fünf Designprinzipien, die darauf abzielen, die Abhängigkeiten zwischen Klassen zu minimieren und die Flexibilität des Codes zu erhöhen. Im "Haushaltsplangenerator" haben wir diese Prinzipien konsequent angewendet, um die Wartbarkeit und Erweiterbarkeit der Software zu verbessern.

1. Single Responsibility Principle (SRP): Jede Klasse sollte nur eine einzige Verantwortung haben und nur für eine spezifische Aufgabe zuständig sein. Im "Haushaltsplangenerator" ist beispielsweise die Klasse "Haushaltsposten" ausschließlich für die Speicherung und Kategorisierung von Projekten zuständig. Sie übernimmt nicht die direkte Speicherung von Ausgaben oder Einnahmen, sondern konzentriert sich nur auf ihre spezifische Aufgabe der Verwaltung von Projekten.

2. Open/Closed Principle (OCP): Softwareentitäten sollten offen für Erweiterungen, aber geschlossen für Modifikationen sein. Im "Haushaltsplangenerator" sind die Klassen "Haushaltsposten" und "Projekt" in sich geschlossen, aber sie können in anderen Plänen genutzt werden, falls das Projekt auf standortübergreifende Planstrukturen erweitert wird. Die Aufteilung in viele eigenständige Klassen ermöglicht es uns, die Software offen für Erweiterungen zu halten, ohne den bestehenden Code zu ändern.

3. Liskov Substitution Principle (LSP): Im "Haushaltsplangenerator" können Ausgaben und Einnahmen verändert werden, ohne Änderungen im darüber liegenden Projekt oder im darüber liegenden Haushaltsposten vorzunehmen. Dies bedeutet, dass die Klassen, die die Ausgaben und Einnahmen nutzen, problemlos mit anderen Subtypen von Ausgaben und Einnahmen arbeiten können, ohne dass dies die Funktionalität der Software beeinträchtigt. Dadurch wird die Interoperabilität und Austauschbarkeit von Klassen gefördert.

4. Interface Segregation Principle (ISP): Im "Haushaltsplangenerator" kann für Interface Segregation Principle das gleiche Beispiel wie beim Liskov Substitution Principle angewendet werden, um es zu veranschaulichen. Clienten, die Projekte ändern, benötigen dafür nicht die Klasse "Haushaltsplan". Die Trennung von großen Schnittstellen in spezifischere Teile reduziert die Kopplung und erhöht die Flexibilität des Codes.

5. Dependency Inversion Principle (DIP): Im "Haushaltsplangenerator" werden Abhängigkeiten zwischen den Klassen "Haushaltsplan", "Haushaltsposten", "Projekt" und "Aufwand" nur auf die Klasse als Objekt-Ebene eingebunden und nicht auf die spezielle Implementierungsebene. Beispielsweise greift das Projekt nicht auf die spezielle Implementierung der Werteberechnung und der Einnahmen/Ausgaben-Felder im Aufwand zu, sondern es referenziert lediglich den Aufwand selbst. Dadurch bleibt die Flexibilität des Codes erhalten und Abhängigkeiten können leichter ausgetauscht werden.

#### GRASP-Prinzipien

Die GRASP-Prinzipien (General Responsibility Assignment Software Patterns) sind ein Satz von Entwurfsrichtlinien, die helfen, die Verantwortlichkeiten und Zusammenhänge zwischen Klassen zu definieren. Im "Haushaltsplangenerator" haben wir die GRASP-Prinzipien angewendet, um eine klare und effiziente Strukturierung des Codes zu erreichen.

1. Creator: Objekte sollten nur dann Verantwortung für die Erstellung von anderen Objekten übernehmen, wenn sie eine logische Beziehung zu diesen Objekten haben. Im "Haushaltsplangenerator" wird die Erstellung von Objekten immer durch die `create`-Methode in den entsprechenden Klassen selbst durchgeführt. Beispielsweise ruft die Klasse "Haushaltsposten" als einziges die `create`-Methode der Klasse "Projekt" auf, und die Klasse "Projekt" als einziges die `create`-Methode von "Aufwand" auf.

2. Information Expert: Eine Verantwortlichkeit sollte einem Objekt zugewiesen werden, das über die notwendigen Informationen verfügt, um diese Verantwortung zu erfüllen. Im "Haushaltsplangenerator" wird das Erstellen von Objekten und deren Zuordnung immer von der übergeordneten Klasse im Haushaltsplan (HHP) übernommen. Die Klasse "Haushaltsplan" hat beispielsweise die notwendigen Informationen, um Haushaltsposten zu erstellen und diesen die entsprechenden Aufwände zuzuordnen.

3. Low Coupling: Klassen sollten möglichst unabhängig voneinander sein, um die Flexibilität und Wartbarkeit des Codes zu erhöhen. Im "Haushaltsplangenerator" haben die Klassen "Aufwand", "Projekt", "Haushaltsposten" und "Haushaltsplan" untereinander Abhängigkeiten. Jedoch sind die Abhängigkeiten so organisiert, dass beispielsweise "Haushaltsposten" und "Aufwand" nicht voneinander abhängig sind, sondern immer nur von der darüber oder darunter liegenden Größenordnung im Haushaltsplan. Dies reduziert die Kopplung zwischen den Klassen und erhöht die Flexibilität der Software.

4. High Cohesion: Klassen sollten eng zusammenhängende Funktionen haben und nur solche Methoden und Eigenschaften enthalten, die für die Erfüllung ihrer Verantwortlichkeiten relevant sind. Im "Haushaltsplangenerator" hat beispielsweise der Haushaltsplan alle Methoden zum Erhalt von Informationen über die Haushaltsposten und Aufwände, führt aber keine Berechnungen durch, die im Aufgabenbereich der Haushaltsposten oder Aufwände stehen. Jede Klasse konzentriert sich auf ihre spezifischen Aufgaben, was die Wartbarkeit und Lesbarkeit des Codes verbessert.

5. Polymorphism: Im aktuellen Use Case des "Haushaltsplangenerators" wurden keine eigen erstellten Klassen erstellt, die mehrere eigen erstellte Unterklassen haben, da der Use Case dafür nicht besonders geeignet war. Jedoch bietet das Prinzip des Polymorphismus die Möglichkeit, bei einer möglichen zukünftigen Erweiterung für Haushaltspläne anderer Gremien beispielsweise Haushaltsposten und Geschäftsposten als Unterklasse von "Posten" zu implementieren. Dies ermöglicht eine einheitliche Behandlung verschiedener Posten-Typen und erhöht die Flexibilität und Erweiterbarkeit der Software.

Durch die Anwendung der SOLID- und GRASP-Prinzipien haben wir im "Haushaltsplangenerator" eine saubere und gut strukturierte Codebasis geschaffen, die leicht erweiterbar, wartbar und effizient ist. Diese Prinzipien bilden eine solide Grundlage für die Weiterentwicklung und Verbesserung der Software.


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

#### 4.3.1 Strategy Pattern

Das Strategy Pattern wird im Haushaltsplangenerator verwendet, um verschiedene Strategien für die Verarbeitung von Haushaltsplänen und Haushaltsposten zu implementieren. Es ermöglicht die flexible Auswahl einer bestimmten Strategie zur Laufzeit, je nachdem, welche Aktion vom Benutzer ausgelöst wird.

Die Anwendung des Strategy Patterns ist in der Klasse "HHPG/application/create_Haushaltsplan.py" zu finden. Dort wird die Klasse `HaushaltsplanStrategy` als abstrakte Basisklasse definiert, die eine Methode `handle_post_request` enthält. Diese Methode wird in den konkreten Strategien überschrieben, um spezifische Verarbeitungslogik zu implementieren.

Ein Beispiel für eine konkrete Strategie ist die Klasse `ExcelExportStrategy`. Diese Strategie wird ausgewählt, wenn der Benutzer einen Haushaltsplan in eine Excel-Datei exportieren möchte. In der `handle_post_request`-Methode der `ExcelExportStrategy` wird der `HaushaltsplanExcelGenerator` verwendet, um die Excel-Datei zu generieren und anschließend dem Benutzer eine Erfolgsmeldung anzuzeigen.

Hier ist der relevante Teil des Codes, in dem das Strategy Pattern angewendet wird:

```python
# Strategy Pattern
class HaushaltsplanStrategy:
    def handle_post_request(self, haushaltsplan, haushaltsposten_list):
        pass

class ExcelExportStrategy(HaushaltsplanStrategy):
    def handle_post_request(self, haushaltsplan, haushaltsposten_list):
        excel_generator = HaushaltsplanExcelGenerator(haushaltsplan)
        excel_generator.generate_excel('haushaltsplan.xlsx')
        return render(request, 'success.html')
```

Hier wird die abstrakte Klasse `HaushaltsplanStrategy` definiert, die eine Methode `handle_post_request` enthält. Die konkrete Klasse `ExcelExportStrategy` erbt von `HaushaltsplanStrategy` und überschreibt die `handle_post_request`-Methode, um die spezifische Logik für den Excel-Export zu implementieren.

Im Code der Klasse `HaushaltsplanView` wird das Strategy Pattern verwendet, indem eine Instanz der `ExcelExportStrategy` erstellt wird und diese Strategie dann verwendet wird, um den Excel-Export durchzuführen:

```python
    def handle_post_request(self, request):
        # ... Andere Code ...

        if haushaltsplan_form.is_valid() and haushaltsposten_formset.is_valid() and projekt_formset.is_valid():
            # ... Andere Code ...

            # Strategy Pattern
            strategy = ExcelExportStrategy()
            return strategy.handle_post_request(haushaltsplan, haushaltsposten_list)
```

Hier wird die `ExcelExportStrategy` instanziiert und ihre `handle_post_request`-Methode aufgerufen, um den Excel-Export durchzuführen.

[Link zur Klasse create_Haushaltsplan.py im GitHub-Repository](https://github.com/Lukas-Hoernle/Advanced-Software-Engineering/blob/Analyse-und-Design/HHPG/application/create_Haushaltsplan.py)

Durch die Anwendung des Strategy Patterns wird die Verarbeitungslogik flexibel und austauschbar gestaltet, da verschiedene Strategien je nach Bedarf verwendet werden können, ohne den gesamten Code zu ändern. Dadurch wird die Erweiterbarkeit und Wartbarkeit des Haushaltsplangenerators verbessert.

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
