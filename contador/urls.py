from django.urls import path
from .views import contar_letras

urlpatterns = [
    path('', contar_letras, name='contar_letras'),
]
