from HHPG.infrastruktur.projekt_repository import ProjektRepository
from django.shortcuts import render


class IndexView:
    service = ProjektRepository()

    @classmethod
    def test(cls, request):
        dingens = cls.service.get_all()[0]

        context = {
            'test': dingens
        }

        return render(request, 'HHPG/test.html', context)
