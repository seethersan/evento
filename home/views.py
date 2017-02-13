from django.shortcuts import render
from django.views.generic import TemplateView
from evento.models import Evento

# Create your views here.


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contexto = super(Home, self).get_context_data(**kwargs)
        contexto['eventos'] = Evento.objects.all().order_by('-id')[:3]
        return contexto