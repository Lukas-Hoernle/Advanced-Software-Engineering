from HHPG.domain.entity.haushaltsplan import Haushaltsplan
from HHPG.infrastruktur.haushaltsplan_repository import HaushaltsplanRepository


class BudgetBerechner:
    def __init__(self, haushaltsplan: Haushaltsplan):
        self.haushaltsplan = HaushaltsplanRepository().get_by_id_including_children(haushaltsplan_id=haushaltsplan.id)

    def ist_verlustbehaftet(self):
        einnahmen, ausgaben = HaushaltsplanRepository().get_aufwaende_of_id(haushaltsplan_id=self.haushaltsplan.id)

        budget = self.haushaltsplan.studierendenzahl * self.haushaltsplan.studierendenbeitrag + einnahmen
        return budget, ausgaben
