from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Alvo
from .forms import AlvosForm
from django.urls import reverse_lazy

class AdicionarAlvoView(CreateView):
    model = Alvo
    form_class = AlvosForm
    template_name='alvos/formulario-alvo.html'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('core:index')


class EditarAlvoView(UpdateView):
    model = Alvo
    form_class = AlvosForm
    template_name='alvos/formulario-alvo-editar.html'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('core:index')


class ExcluirAlvoView(DeleteView):
    model = Alvo
    template_name = 'core/mapa.html'
    success_url = reverse_lazy('core:index')
