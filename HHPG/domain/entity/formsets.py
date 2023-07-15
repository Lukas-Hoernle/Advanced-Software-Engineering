from django.forms import inlineformset_factory

from HHPG.application.forms.HaushaltspostenForm import HaushaltspostenForm
from HHPG.domain.entity.haushaltsplan import Haushaltsplan
from HHPG.domain.entity.haushaltsposten import Haushaltsposten

HaushaltsplanFormSet = inlineformset_factory(
    Haushaltsplan,
    Haushaltsposten,
    HaushaltspostenForm,
    extra=1,
    min_num=1,
)
