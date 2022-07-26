from django.shortcuts import render

from django.views.generic import ListView
from .models import Autor


class ListAutores(ListView):
    model = Autor
    context_object_name: 'lista_autores'
    template_name = 'autor/lista.html'


