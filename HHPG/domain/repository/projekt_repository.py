from django.db.models import QuerySet
from HHPG.domain.entity.projekt import Projekt
from HHPG.domain.repository.projekt_repository import IProjektRepository

from django.db.models import QuerySet
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProjektRepository(IProjektRepository):
    @staticmethod
    @receiver(post_save, sender=Projekt)
    def create(self, sender, instance, **kwargs) -> Projekt:
        return Projekt.objects.create(**instance)

    def save(self, sender, instance, **kwargs) -> None:
        instance.save()

    def delete(self, projekt_id: int) -> None:
        Projekt.objects.filter(id=projekt_id).delete()

    def get_by_id(self, projekt_id) -> Projekt:
        return Projekt.objects.get(id=projekt_id)

    def get_all(self) -> QuerySet:
        raise NotImplementedError

    def order_by(self, order: str) -> QuerySet:
        raise NotImplementedError

    def get_count(self, haushaltsposten_id: int) -> int:
        raise NotImplementedError

    def get_all_by_haushaltsposten(self, haushaltsposten_id: int) -> QuerySet:
        raise NotImplementedError

    def get_all_by_name(self, name: str) -> QuerySet:
        raise NotImplementedError

    def get_all_by_einnahmen(self, einnahmen: int) -> QuerySet:
        raise NotImplementedError

    def update_haushaltsposten(self, projekt_id: int, haushaltsposten) -> None:
        raise NotImplementedError

    def get_haushaltsposten(self, projekt_id: int):
        raise NotImplementedError

    def update_name(self, projekt_id: int, name: str) -> None:
        raise NotImplementedError

    def get_name(self, projekt_id: int):
        projekt = Projekt.objects.get(id=projekt_id)
        return projekt.name

    def update_einnahmen(self, projekt_id: int, einnahmen: int) -> None:
        projekt = Projekt.objects.get(id=projekt_id)
        if projekt.aufwand is not None:
            projekt.aufwand.einnahmen = einnahmen
            projekt.aufwand.save()

    def get_einnahmen(self, projekt_id: int):
        projekt = Projekt.objects.get(id=projekt_id)
        if projekt.aufwand is not None:
            return projekt.aufwand.einnahmen
        return 0

    def update_ausgaben(self, projekt_id: int, ausgaben: int) -> None:
        projekt = Projekt.objects.get(id=projekt_id)
        if projekt.aufwand is not None:
            projekt.aufwand.ausgaben = ausgaben
            projekt.aufwand.save()

    def get_ausgaben(self, projekt_id: int):
        projekt = Projekt.objects.get(id=projekt_id)
        if projekt.aufwand is not None:
            return projekt.aufwand.ausgaben
        return 0

    def get_gewinn(self, projekt_id: int):
        projekt = Projekt.objects.get(id=projekt_id)
        if projekt.aufwand is not None:
            return projekt.aufwand.einnahmen - projekt.aufwand.ausgaben
        return 0
