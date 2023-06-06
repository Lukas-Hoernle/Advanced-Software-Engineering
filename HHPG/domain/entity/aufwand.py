class Aufwand:
    def __init__(self, einnahmen: int, ausgaben: int):
        self.einnahmen = einnahmen
        self.ausgaben = ausgaben

    def get_einnahmen(self) -> int:
        return self.einnahmen

    def set_einnahmen(self, einnahmen: int) -> None:
        self.einnahmen = einnahmen

    def get_ausgaben(self) -> int:
        return self.ausgaben

    def set_ausgaben(self, ausgaben: int) -> None:
        self.ausgaben = ausgaben

    def get_gewinn(self) -> int:
        return self.einnahmen - self.ausgaben
