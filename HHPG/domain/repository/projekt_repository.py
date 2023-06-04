from abc import ABC, abstractmethod

from django.db.models import QuerySet

from HHPG.domain.entity.projekt import Projekt
#todo: rework object model

class IProjektRepository(ABC):

    @abstractmethod
    def create(sender, instance, **kwargs) -> Projekt:
        raise NotImplementedError

    @abstractmethod
    def save(self, sender, instance, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, projekt_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, projekt_id) -> Projekt:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> QuerySet:
        raise NotImplementedError

    @abstractmethod
    def order_by(self, order: str) -> QuerySet:
        raise NotImplementedError

    @abstractmethod
    def get_count(self, haushaltsposten_id: int) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_all_by_haushaltsposten(self, haushaltsposten_id: int) -> QuerySet:
        raise NotImplementedError

    @abstractmethod
    def get_all_by_name(self, name: str) -> QuerySet:
        raise NotImplementedError

    @abstractmethod
    def get_all_by_einnahmen(self, einnahmen: int) -> QuerySet:
        raise NotImplementedError

    @abstractmethod
    def update_haushaltsposten(self, projekt_id: int, haushaltsposten) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_haushaltsposten(self, projekt_id: int):
        raise NotImplementedError

    @abstractmethod
    def update_name(self, projekt_id: int, name: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_name(self, projekt_id: int):
        raise NotImplementedError

    @abstractmethod
    def update_einnahmen(self, projekt_id: int, einnahmen: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_einnahmen(self, projekt_id: int):
        raise NotImplementedError
