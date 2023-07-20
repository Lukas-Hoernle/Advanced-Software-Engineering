from django.db.models import QuerySet
from HHPG.domain.entity.projekt import Projekt
from HHPG.domain.repository.projekt_repository import IProjektRepository

from django.db.models import QuerySet
from django.db.models.signals import post_save
from django.dispatch import receiver

from HHPG.infrastruktur.aufwand_repository import AufwandRepository


class ProjektRepository(IProjektRepository):
    @staticmethod
    @receiver(post_save, sender=Projekt)
    def create(sender, instance, created, **kwargs) -> Projekt | None:
        if created:
            return None

        return Projekt.objects.create(**instance)

    def save(self, sender, instance, **kwargs) -> None:
        instance.save()

    def delete(self, projekt_id: int) -> None:
        Projekt.objects.filter(id=projekt_id).delete()

    def get_by_id(self, projekt_id) -> Projekt:
        return Projekt.objects.get(id=projekt_id)

    def get_all(self) -> QuerySet:
        return Projekt.objects.all()

    def order_by(self, order: str) -> QuerySet:
        return Projekt.objects.order_by(order)

    def get_count(self, haushaltsposten_id: int) -> int:
        return Projekt.objects.filter(haushaltsposten_id=haushaltsposten_id).count()

    def get_all_by_haushaltsposten(self, haushaltsposten_id: int) -> QuerySet:
        return Projekt.objects.filter(haushaltsposten_id=haushaltsposten_id)

    def get_all_by_haushaltsposten_including_children(self, haushaltsposten_id: int) -> QuerySet:
        projekt_liste = self.get_all_by_haushaltsposten(haushaltsposten_id=haushaltsposten_id)
        for projekt in projekt_liste:
            projekt.aufwand = AufwandRepository().get_for_projekt(projekt.id)

        return projekt_liste

    def get_all_by_name(self, name: str) -> QuerySet:
        return Projekt.objects.filter(name=name)

    def get_all_by_einnahmen(self, einnahmen: int) -> QuerySet:
        return Projekt.objects.filter(aufwand__einnahmen=einnahmen)

    def update_haushaltsposten(self, projekt_id: int, haushaltsposten) -> None:
        projekt = Projekt.objects.get(id=projekt_id)
        projekt.haushaltsposten = haushaltsposten
        projekt.save()

    def get_haushaltsposten(self, projekt_id: int):
        projekt = Projekt.objects.get(id=projekt_id)
        return projekt.haushaltsposten

    def update_name(self, projekt_id: int, name: str) -> None:
        projekt = Projekt.objects.get(id=projekt_id)
        projekt.projekt_name = name
        projekt.save()

    def get_name(self, projekt_id: int):
        projekt = Projekt.objects.get(id=projekt_id)
        return projekt.projekt_name

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

    def get_ausgaben(self, projekt_id: int) -> int:
        projekt = Projekt.objects.get(id=projekt_id)
        if projekt.aufwand is not None:
            return projekt.aufwand.ausgaben
        return 0

    def get_gewinn(self, projekt_id: int) -> int:
        projekt = Projekt.objects.get(id=projekt_id)
        if projekt.aufwand is not None:
            return projekt.aufwand.einnahmen - projekt.aufwand.ausgaben
        return 0
