from django.shortcuts import render
from .models import ProjetoDjango


def homepage(request):
    return render(
                    request=request,
                    template_name="home.html",
                    context={"Filmes": ProjetoDjango.objects.all}
                )