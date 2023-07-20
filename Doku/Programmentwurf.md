
## 5. Implementierung

### 5.1 Umsetzung der Schichtenarchitektur

Die zuvor geplante Schichtenarchitektur (siehe Kapitel 4.2.1) wurde während der Implementierung praktisch umgesetzt. Jede Schicht wurde klar voneinander getrennt, um die Verantwortlichkeiten zu isolieren und die Wartbarkeit der Software zu verbessern.

#### Interaktion der Schichten

Die Schichten interagieren miteinander über klar definierte Schnittstellen. Die Präsentationsschicht kommuniziert mit der Anwendungsschicht, indem sie die Anwendungslogik aufruft, um Aktionen des Benutzers zu verarbeiten. Die Anwendungsschicht greift wiederum auf die Domain-Schicht zu, um die Geschäftslogik und -regeln umzusetzen. Die Domain-Schicht enthält die Entities, Value Objects und Repositories, die das Kerngeschäft des Haushaltsplangenerators ausmachen. Die Infrastruktur-Schicht kümmert sich um technische Details wie Datenbankanbindung und externe Datenquellen.

Durch diese klare Trennung der Verantwortlichkeiten ist die Architektur gut strukturiert und erleichtert die Wartbarkeit und Erweiterbarkeit des Haushaltsplangenerators.

#### Vorteile und Herausforderungen der Schichtenarchitektur

Die Schichtenarchitektur bietet mehrere Vorteile während der Implementierung. Die klare Trennung der Verantwortlichkeiten ermöglicht es, einzelne Schichten unabhängig voneinander zu entwickeln und zu testen. Dadurch wird der Code besser strukturiert und leichter verständlich. Änderungen in einer Schicht haben weniger Auswirkungen auf andere Schichten, was die Wartbarkeit erhöht.

Die Herausforderungen der Schichtenarchitektur bestehen darin, die Kommunikation zwischen den Schichten effizient zu gestalten. Der Overhead durch die Verwendung von Schnittstellen kann in manchen Fällen die Leistung beeinträchtigen. Es ist wichtig, die Schnittstellen sorgfältig zu gestalten, um die Performance zu optimieren.

### 5.2 Implementierung der Domain-Logik

Die Domain-Logik des Haushaltsplangenerators wurde detailliert umgesetzt. Die Entities repräsentieren die Hauptobjekte des Systems wie Haushaltspläne, Haushaltsposten und Projekte. Value Objects wurden verwendet, um unveränderliche Werte wie Datumsbereiche darzustellen. Repositories bieten eine Schnittstelle zur Datenbank und ermöglichen den Zugriff auf die Entities.

Die Geschäftsregeln und -logik wurden in den entsprechenden Klassen der Domain-Schicht umgesetzt. Beispielsweise wurden Validierungen in den Entities implementiert, um sicherzustellen, dass nur korrekte Daten gespeichert werden. Die Verarbeitung von Geschäftsregeln erfolgte in den entsprechenden Services der Anwendungsschicht.

Die saubere Trennung zwischen der Domain-Schicht und anderen Schichten erleichterte das Testen der Geschäftslogik und trug zur Entkopplung des Codes bei.

### 5.3 Einbindung von externen Datenquellen

Während der Implementierung wurden externe Datenquellen in den Haushaltsplangenerator eingebunden. Dazu gehörten zum Beispiel APIs zur Abfrage von Währungskursen oder Datenbanken zur Speicherung von Benutzerinformationen.

Die Integration externer Datenquellen erfolgte über entsprechende Schnittstellen und Adapter. Externe Daten wurden abgerufen, verarbeitet und in das interne Format des Haushaltsplangenerators umgewandelt, um eine nahtlose Interaktion zu gewährleisten.

Herausforderungen bei der Einbindung externer Datenquellen bestanden in der Handhabung von Fehlern und Ausfällen dieser Quellen. Es war wichtig, robuste Mechanismen zu implementieren, um mit unerwarteten Situationen umgehen zu können und die Stabilität der Anwendung zu gewährleisten.

### 5.4 Unit Testing (Einsatz und Begründung von Unit Tests und Mocks)

Unit Tests wurden als zentrales Element für die Qualitätssicherung und Fehlererkennung in der Software eingesetzt. Für jede Schicht wurden separate Tests geschrieben, um sicherzustellen, dass die einzelnen Komponenten korrekt funktionieren.

Die Unit Tests deckten verschiedene Testfälle ab, einschließlich positiver und negativer Szenarien. Sie halfen dabei, Fehler frühzeitig zu erkennen und die Softwarequalität zu verbessern.

Mocks wurden in den Unit Tests verwendet, um externe Abhängigkeiten zu isolieren und die Tests unabhängig von externen Ressourcen auszuführen. Dies trug dazu bei, die Testgeschwindigkeit zu erhöhen und die Tests besser zu kontrollieren.

Der Einsatz von Unit Tests hatte einen positiven Einfluss auf die Gesamtqualität des Projekts, da die Entwickler mehr Vertrauen in den Code hatten und Änderungen mit größerer Sicherheit vornehmen konnten. Obwohl das Schreiben von Unit Tests zusätzlichen Aufwand erforderte, zahlte es sich durch die Reduzierung von Fehlern und die einfachere Wartung langfristig aus.

Die Implementierung von Unit Tests hat jedoch auch die Entwicklungszeit etwas verlängert. Es war wichtig, einen angemessenen Aufwand für die Testabdeckung festzulegen, um den richtigen Kompromiss zwischen Qualitätssicherung und Entwicklungseffizienz zu finden.

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
