from django.urls import path

from apps.usuarios.views import UsuarioListView

urlpatterns = [
    path(route='',
         view=UsuarioListView,
         name='index')
]
