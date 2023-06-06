from abc import ABC, abstractmethod
from typing import List

from HHPG.domain.entity.aufwand import Aufwand


class IAufwandRepository(ABC):
    @abstractmethod
    def create(self, einnahmen: int, ausgaben: int) -> Aufwand:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, aufwand_id: int) -> Aufwand:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[Aufwand]:
        raise NotImplementedError

    @abstractmethod
    def update_einnahmen(self, aufwand_id: int, einnahmen: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def update_ausgaben(self, aufwand_id: int, ausgaben: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, aufwand_id: int) -> None:
        raise NotImplementedError


class AufwandRepository(IAufwandRepository):
    def create(self, einnahmen: int, ausgaben: int) -> Aufwand:
        aufwand = Aufwand(einnahmen=einnahmen, ausgaben=ausgaben)
        return aufwand

    def get_by_id(self, aufwand_id: int) -> Aufwand:
        raise NotImplementedError

    def get_all(self) -> List[Aufwand]:
        raise NotImplementedError

    def update_einnahmen(self, aufwand_id: int, einnahmen: int) -> None:
        aufwand = self.get_by_id(aufwand_id)
        aufwand.set_einnahmen(einnahmen)

    def update_ausgaben(self, aufwand_id: int, ausgaben: int) -> None:
        aufwand = self.get_by_id(aufwand_id)
        aufwand.set_ausgaben(ausgaben)

    def delete(self, aufwand_id: int) -> None:
        raise NotImplementedError
