from django.forms import inlineformset_factory

from HHPG.application.forms.AufwandForm import AufwandForm
from HHPG.application.forms.HaushaltspostenForm import HaushaltspostenForm
from HHPG.application.forms.ProjektForm import ProjektForm
from HHPG.domain.entity.aufwand import Aufwand
from HHPG.domain.entity.haushaltsplan import Haushaltsplan
from HHPG.domain.entity.haushaltsposten import Haushaltsposten
from HHPG.domain.entity.projekt import Projekt

HaushaltsplanFormSet = inlineformset_factory(
    Haushaltsplan,
    Haushaltsposten,
    fields=(
        'name',
    ),
    extra=1,
    min_num=1,
)

HaushaltspostenFormSet = inlineformset_factory(
    Haushaltsposten,
    Projekt,
    fields=(
        'name',
    ),
    extra=1,
    min_num=1,
)

ProjektFormSet = inlineformset_factory(
    Projekt,
    Aufwand,
    fields=(
        'einnahmen',
        'ausgaben',
    ),
    extra=1,
    min_num=1,
)
