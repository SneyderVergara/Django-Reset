from django.shortcuts import HttpResponse
from django.shortcuts import render

from .models import *

from rest_framework import viewsets
from .serializers import *
# Create your views here.

def index(request):
    return HttpResponse("Hola mundo Django-Rest.")

# Vistas para el conjunto de datos de las API
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
