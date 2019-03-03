from django.urls import path
from .views import *

urlpatterns = [
    path('$/',home, name = 'index'),
    path('agregarUsuario/',CrearUsuario.as_view(), name = 'agregarUsuario'),
    path('listarUsuario/',ListUsuario.as_view(), name = 'listarUsuario'),
    path('modificarUsuario/<int:pk>',UpdateUsuario.as_view(), name = 'modificarUsuario'),
    #path('modificarUsuario/<int:id>', modificarUsuario, name='modificarUsuario'),
    path('eliminarUsuario/<int:pk>',DeleteUsuario.as_view(), name = 'eliminarUsuario'),
    #path('eliminarUsuario/<int:id>', eliminarUsuario, name='eliminarUsuario'),
]