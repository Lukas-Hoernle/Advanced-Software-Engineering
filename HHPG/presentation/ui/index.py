from HHPG.application.forms.HaushaltsplanForm import HaushaltsplanForm
from django.shortcuts import render


class IndexView:
    @classmethod
    def index(cls, request):
        if request.method == 'POST':
            form = HaushaltsplanForm(request.POST)
            if form.is_valid():
                haushaltsplan = form.save()
                # Do something with the created haushaltsplan object
        else:
            form = HaushaltsplanForm()

        context = {
            'form': form
        }

        return render(request, 'test.html', context)
