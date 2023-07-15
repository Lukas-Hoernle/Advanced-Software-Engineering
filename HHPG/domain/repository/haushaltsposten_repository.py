from abc import ABC, abstractmethod

from django.db.models import QuerySet

from HHPG.domain.entity.haushaltsplan import Haushaltsplan
from HHPG.domain.entity.haushaltsposten import Haushaltsposten


class IHaushaltspostenRepository(ABC):

    @abstractmethod
    def create(sender, instance, **kwargs) -> Haushaltsposten:
        raise NotImplementedError

    @abstractmethod
    def save(self, sender, instance, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, haushaltsposten_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, haushaltsposten_id: int) -> Haushaltsposten:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> QuerySet:
        raise NotImplementedError

    @abstractmethod
    def get_all_by_haushaltsplan(self, haushaltsplan: Haushaltsplan) -> QuerySet:
        raise NotImplementedError

    @abstractmethod
    def update_haushaltsplan(self, haushaltsposten_id: int, haushaltsplan: Haushaltsplan) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_haushaltsplan(self, haushaltsposten_id: int) -> Haushaltsplan:
        raise NotImplementedError

    @abstractmethod
    def update_name(self, haushaltsposten_id: int, name: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_name(self, haushaltsposten_id: int) -> str:
        raise NotImplementedError
