from abc import ABC, abstractmethod

from django.contrib.auth.models import User
from django.db.models import QuerySet

from HHPG.domain.entity.haushaltsplan import Haushaltsplan


class IHaushaltsplanRepository(ABC):

    @abstractmethod
    def create(self, name: str, standort: str, startjahr: int, autor: User, studierendenzahl: int) -> Haushaltsplan:
        raise NotImplementedError

    @abstractmethod
    def save(self, haushaltsplan: Haushaltsplan) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, haushaltsplan_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, haushaltsplan_id: int) -> Haushaltsplan:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> QuerySet:
        raise NotImplementedError

    @abstractmethod
    def update_name(self, haushaltsplan_id: int, name: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_name(self, haushaltsplan_id: int) -> str:
        raise NotImplementedError

    @abstractmethod
    def update_standort(self, haushaltsplan_id: int, standort: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_standort(self, haushaltsplan_id: int) -> str:
        raise NotImplementedError

    @abstractmethod
    def update_startjahr(self, haushaltsplan_id: int, startjahr: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_startjahr(self, haushaltsplan_id: int) -> int:
        raise NotImplementedError

    @abstractmethod
    def update_autor(self, haushaltsplan_id: int, autor: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_autor(self, haushaltsplan_id: int) -> User:
        raise NotImplementedError

    @abstractmethod
    def update_studierendenzahl(self, haushaltsplan_id: int, studierendenzahl: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_studierendenzahl(self, haushaltsplan_id: int) -> int:
        raise NotImplementedError
