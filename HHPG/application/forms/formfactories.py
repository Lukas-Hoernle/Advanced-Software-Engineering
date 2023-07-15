from django.forms import inlineformset_factory

from HHPG.domain.entity.aufwand import Aufwand
from HHPG.domain.entity.haushaltsplan import Haushaltsplan
from HHPG.domain.entity.haushaltsposten import Haushaltsposten
from HHPG.domain.entity.projekt import Projekt

HaushaltspostenFormSet = inlineformset_factory(
    Haushaltsplan,
    Haushaltsposten,
    fields=['name'],
    extra=1,
    can_delete=True
)

ProjektFormSet = inlineformset_factory(
    Haushaltsposten,
    Projekt,
    fields=['name'],
    extra=1,
    can_delete=True
)