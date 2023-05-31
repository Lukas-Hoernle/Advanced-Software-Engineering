from django.contrib import admin

# Register your models here.

from .domain.entity.haushaltsposten import Haushaltsposten
from .domain.entity.projekt import Projekt
from .domain.entity.haushaltsplan import Haushaltsplan

admin.site.register(Haushaltsposten)
admin.site.register(Projekt)
admin.site.register(Haushaltsplan)
