from django.contrib.auth.models import User
from django.db.models import QuerySet

from .haushaltsposten_repository import HaushaltspostenRepository
from .projekt_repository import ProjektRepository
from ..domain.entity.haushaltsplan import Haushaltsplan
from ..domain.repository.haushaltsplan_repository import IHaushaltsplanRepository


class HaushaltsplanRepository(IHaushaltsplanRepository):
    def create(self, sender, instance, **kwargs) -> Haushaltsplan:
        return Haushaltsplan.objects.create(**instance)

    def save(self, sender, instance, **kwargs) -> None:
        instance.save()

    def delete(self, haushaltsplan_id: int) -> None:
        Haushaltsplan.objects.filter(id=haushaltsplan_id).delete()

    def get_by_id(self, haushaltsplan_id: int) -> Haushaltsplan:
        return Haushaltsplan.objects.get(id=haushaltsplan_id)

    def get_by_id_including_children(self, haushaltsplan_id: int) -> Haushaltsplan:
        haushaltsplan = self.get_by_id(haushaltsplan_id=haushaltsplan_id)
        haushaltsplan.haushaltsposten_liste = HaushaltspostenRepository().get_all_by_haushaltsplan_including_children(
            haushaltsplan=haushaltsplan)
        return haushaltsplan

    def get_aufwaende_of_id(self, haushaltsplan_id: int) -> (int, int):
        einnahmen = 0
        ausgaben = 0

        haushaltsplan = self.get_by_id(haushaltsplan_id=haushaltsplan_id)
        haushaltsposten_liste = HaushaltspostenRepository().get_all_by_haushaltsplan(haushaltsplan=haushaltsplan)

        for haushaltsposten in haushaltsposten_liste:
            _einnahmen, _ausgaben = ProjektRepository().get_aufwaende_of_id(haushaltsposten_id=haushaltsposten.id)
            einnahmen += _einnahmen
            ausgaben += _ausgaben

        return einnahmen, ausgaben

    def get_all(self) -> QuerySet:
        return Haushaltsplan.objects.all()

    def update_name(self, haushaltsplan_id: int, name: str) -> None:
        haushaltsplan = Haushaltsplan.objects.get(id=haushaltsplan_id)
        haushaltsplan.plan_name = name
        haushaltsplan.save()

    def get_name(self, haushaltsplan_id: int) -> str:
        haushaltsplan = Haushaltsplan.objects.get(id=haushaltsplan_id)
        return haushaltsplan.plan_name

    def update_standort(self, haushaltsplan_id: int, standort: str) -> None:
        haushaltsplan = Haushaltsplan.objects.get(id=haushaltsplan_id)
        haushaltsplan.standort = standort
        haushaltsplan.save()

    def get_standort(self, haushaltsplan_id: int) -> str:
        haushaltsplan = Haushaltsplan.objects.get(id=haushaltsplan_id)
        return haushaltsplan.standort

    def update_startjahr(self, haushaltsplan_id: int, startjahr: int) -> None:
        haushaltsplan = Haushaltsplan.objects.get(id=haushaltsplan_id)
        haushaltsplan.startjahr = startjahr
        haushaltsplan.save()

    def get_startjahr(self, haushaltsplan_id: int) -> int:
        haushaltsplan = Haushaltsplan.objects.get(id=haushaltsplan_id)
        return haushaltsplan.startjahr

    def update_autor(self, haushaltsplan_id: int, autor: User) -> None:
        haushaltsplan = Haushaltsplan.objects.get(id=haushaltsplan_id)
        haushaltsplan.autor = autor
        haushaltsplan.save()

    def get_autor(self, haushaltsplan_id: int) -> User:
        haushaltsplan = Haushaltsplan.objects.get(id=haushaltsplan_id)
        return haushaltsplan.autor

    def update_studierendenzahl(self, haushaltsplan_id: int, studierendenzahl: int) -> None:
        haushaltsplan = Haushaltsplan.objects.get(id=haushaltsplan_id)
        haushaltsplan.studierendenzahl = studierendenzahl
        haushaltsplan.save()

    def get_studierendenzahl(self, haushaltsplan_id: int) -> int:
        haushaltsplan = Haushaltsplan.objects.get(id=haushaltsplan_id)
        return haushaltsplan.studierendenzahl
