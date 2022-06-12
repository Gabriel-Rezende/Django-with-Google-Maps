from django.shortcuts import render
from alvos.models import Alvo
from django.views.generic import ListView
from datetime import date

class MapaView(ListView):
    template_name = "core/mapa.html"
    model = Alvo

    def get_queryset(self):
        data_atual = date.today()
        alvos = Alvo.objects.filter(data_expiracao__gte=data_atual)
        return alvos
