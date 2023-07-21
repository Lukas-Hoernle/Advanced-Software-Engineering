from typing import List

from HHPG.domain.entity.aufwand import Aufwand
from HHPG.domain.repository.aufwand_repository import IAufwandRepository


class AufwandRepository(IAufwandRepository):
    def create(self, einnahmen: int, ausgaben: int) -> Aufwand:
        aufwand = Aufwand(einnahmen=einnahmen, ausgaben=ausgaben)
        aufwand.save()
        return aufwand

    def get_by_id(self, aufwand_id: int) -> Aufwand:
        try:
            aufwand = Aufwand.objects.get(id=aufwand_id)
            return aufwand
        except Aufwand.DoesNotExist:
            return None

    def get_all(self) -> List[Aufwand]:
        return Aufwand.objects.all()

    def get_for_projekt(self, projekt_id: int) -> Aufwand:
        return Aufwand.objects.filter(projekt_id=projekt_id).first()

    def update_einnahmen(self, aufwand_id: int, einnahmen: int) -> None:
        aufwand = self.get_by_id(aufwand_id)
        if aufwand:
            aufwand.einnahmen = einnahmen
            aufwand.save()

    def update_ausgaben(self, aufwand_id: int, ausgaben: int) -> None:
        aufwand = self.get_by_id(aufwand_id)
        if aufwand:
            aufwand.ausgaben = ausgaben
            aufwand.save()

    def delete(self, aufwand_id: int) -> None:
        aufwand = self.get_by_id(aufwand_id)
        if aufwand:
            aufwand.delete()

    def get_aufwaende_of_id(self, projekt_id: int):
        aufwand = self.get_for_projekt(projekt_id=projekt_id)
        return aufwand.einnahmen, aufwand.ausgaben
