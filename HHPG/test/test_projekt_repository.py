from django.db.models import QuerySet
from HHPG.domain.entity.projekt import Projekt
from HHPG.domain.repository.i_projekt_repository import IProjektRepository

class ProjektRepository(IProjektRepository):
    def create(self, name: str, einnahmen: int, ausgaben: int) -> Projekt:
        # Implementierung der create-Methode, um ein neues Projekt zu erstellen
        pass

    def save(self, projekt: Projekt) -> None:
        # Implementierung der save-Methode, um ein Projekt zu speichern/aktualisieren
        pass

    def delete(self, projekt_id: int) -> None:
        # Implementierung der delete-Methode, um ein Projekt zu löschen
        pass

    def get_by_id(self, projekt_id) -> Projekt:
        # Implementierung der get_by_id-Methode, um ein Projekt anhand der ID abzurufen
        pass

    def get_all(self) -> QuerySet:
        # Implementierung der get_all-Methode, um alle Projekte abzurufen
        pass

    def order_by(self, order: str) -> QuerySet:
        # Implementierung der order_by-Methode, um Projekte nach einem Kriterium zu sortieren
        pass

    def get_count(self, haushaltsposten_id: int) -> int:
        # Implementierung der get_count-Methode, um die Anzahl der Projekte für einen Haushaltsposten abzurufen
        pass

    def get_all_by_haushaltsposten(self, haushaltsposten_id: int) -> QuerySet:
        # Implementierung der get_all_by_haushaltsposten-Methode, um Projekte für einen Haushaltsposten abzurufen
        pass

    def get_all_by_name(self, name: str) -> QuerySet:
        # Implementierung der get_all_by_name-Methode, um Projekte anhand des Namens abzurufen
        pass

    def get_all_by_einnahmen(self, einnahmen: int) -> QuerySet:
        # Implementierung der get_all_by_einnahmen-Methode, um Projekte anhand der Einnahmen abzurufen
        pass

    def update_haushaltsposten(self, projekt_id: int, haushaltsposten) -> None:
        # Implementierung der update_haushaltsposten-Methode, um den Haushaltsposten eines Projekts zu aktualisieren
        pass

    def get_haushaltsposten(self, projekt_id: int):
        # Implementierung der get_haushaltsposten-Methode, um den Haushaltsposten eines Projekts abzurufen
        pass

    def update_name(self, projekt_id: int, name: str) -> None:
        # Implementierung der update_name-Methode, um den Namen eines Projekts zu aktualisieren
        pass

    def get_name(self, projekt_id: int):
        # Implementierung der get_name-Methode, um den Namen eines Projekts abzurufen
        pass

    def update_einnahmen(self, projekt_id: int, einnahmen: int) -> None:
        # Implementierung der update_einnahmen-Methode, um die Einnahmen eines Projekts zu aktualisieren
        pass

    def get_einnahmen(self, projekt_id: int):
        # Implementierung der get_einnahmen-Methode, um die Einnahmen eines Projekts abzurufen
        pass

    def update_ausgaben(self, projekt_id: int, ausgaben: int) -> None:
        # Implementierung der update_ausgaben-Methode, um die Ausgaben eines Projekts zu aktualisieren
        pass

    def get_ausgaben(self, projekt_id: int):
        # Implementierung der get_ausgaben-Methode, um die Ausgaben eines Projekts abzurufen
        pass

    def get_gewinn(self, projekt_id: int):
        # Implementierung der get_gewinn-Methode, um den Gewinn eines Projekts abzurufen
        pass
