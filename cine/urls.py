from django.urls import path, include
from rest_framework import routers

from .import views


router = routers.DefaultRouter()
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'pelicula', views.PeliculaViewSet)

urlpatterns = [
    path("", views.index, name="index"),

    path('api/1.0/', include(router.urls))
]
