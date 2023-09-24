from django.urls import include, path
from . import views

urlpatterns = [
    path('prueba/',views.prueba,name='prueba'),
]