from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from docentes.models import Docente

class DocenteList(ListView):
    model = Docente

class DocenteCreate(CreateView):
    model = Docente
    fields = ['nome']
    success_url = reverse_lazy('docentes:docente_list')

class DocenteUpdate(UpdateView):
    model = Docente
    fields = ['nome']
    success_url = reverse_lazy('docentes:docente_list')

class DocenteDelete(DeleteView):
    model = Docente
    success_url = reverse_lazy('docentes:docente_list')
