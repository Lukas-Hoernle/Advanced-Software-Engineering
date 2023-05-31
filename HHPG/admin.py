from django.contrib import admin

# Register your models here.

from .domain.entity.haushaltsposten import Haushaltsposten
from .domain.entity.projekt import Project

admin.site.register(Haushaltsposten)
admin.site.register(Project)
