from django.db.models import QuerySet
from HHPG.domain.entity.haushaltsposten import Haushaltsposten
from .projekt_repository import ProjektRepository
from ..domain.entity.haushaltsplan import Haushaltsplan
from ..domain.repository.haushaltsposten_repository import IHaushaltspostenRepository


class HaushaltspostenRepository(IHaushaltspostenRepository):
    def create(self, sender, instance, **kwargs) -> Haushaltsposten:
        return Haushaltsposten.objects.create(**instance)

    def save(self, sender, instance, **kwargs) -> None:
        instance.save()

    def delete(self, haushaltsposten_id: int) -> None:
        Haushaltsposten.objects.filter(id=haushaltsposten_id).delete()

    def get_by_id(self, haushaltsposten_id: int) -> Haushaltsposten:
        return Haushaltsposten.objects.get(id=haushaltsposten_id)

    def get_all_by_haushaltsplan_including_children(self, haushaltsplan: Haushaltsplan) -> QuerySet:
        haushaltsposten_liste = self.get_all_by_haushaltsplan(haushaltsplan=haushaltsplan)
        for haushaltsposten in haushaltsposten_liste:
            haushaltsposten.projekte = ProjektRepository().get_all_by_haushaltsposten_including_children(
                haushaltsposten_id=haushaltsposten.id)

        return haushaltsposten_liste

    def get_all(self) -> QuerySet:
        return Haushaltsposten.objects.all()

    def get_all_by_haushaltsplan(self, haushaltsplan: Haushaltsplan) -> QuerySet:
        return Haushaltsposten.objects.filter(haushaltsplan=haushaltsplan)

    def update_haushaltsplan(self, haushaltsposten_id: int, haushaltsplan: Haushaltsplan) -> None:
        haushaltsposten = Haushaltsposten.objects.get(id=haushaltsposten_id)
        haushaltsposten.haushaltsplan = haushaltsplan
        haushaltsposten.save()

    def get_haushaltsplan(self, haushaltsposten_id: int) -> Haushaltsplan:
        haushaltsposten = Haushaltsposten.objects.get(id=haushaltsposten_id)
        return haushaltsposten.haushaltsplan

    def update_name(self, haushaltsposten_id: int, name: str) -> None:
        haushaltsposten = Haushaltsposten.objects.get(id=haushaltsposten_id)
        haushaltsposten.posten_name = name
        haushaltsposten.save()

    def get_name(self, haushaltsposten_id: int) -> str:
        haushaltsposten = Haushaltsposten.objects.get(id=haushaltsposten_id)
        return haushaltsposten.posten_name

    def get_aufwaende_by_haushaltsplan(self, haushaltsplan: Haushaltsplan):
        einnahmen = 0
        ausgaben = 0

        haushaltsposten_liste = HaushaltspostenRepository().get_all_by_haushaltsplan(haushaltsplan=haushaltsplan)
        for haushaltsposten in haushaltsposten_liste:
            _einnahmen, _ausgaben = ProjektRepository().get_aufwaende_of_id(haushaltsposten_id=haushaltsposten.id)
            einnahmen += _einnahmen
            ausgaben += _ausgaben

        return einnahmen, ausgaben

    def get_aufwaende_by_haushaltsplan(self, haushaltsplan: Haushaltsplan):
        einnahmen = 0
        ausgaben = 0

        haushaltsposten_liste = HaushaltspostenRepository().get_all_by_haushaltsplan(haushaltsplan=haushaltsplan)
        for haushaltsposten in haushaltsposten_liste:
            _einnahmen, _ausgaben = ProjektRepository().get_aufwaende_of_id(haushaltsposten_id=haushaltsposten.id)
            einnahmen += _einnahmen
            ausgaben += _ausgaben

        return einnahmen, ausgaben
