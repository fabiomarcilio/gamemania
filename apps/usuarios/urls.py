from django.urls import path

from .views import (UsuarioHtmxListView, UsuarioHtmxCreateView,
                    UsuarioHtmxUpdateView, UsuarioHtmxDeleteView,
                    UsuarioTemplateView, RetornarUsuarios)

app_name = 'usuario'

urlpatterns = [
    path(
        route='form',
        view=UsuarioTemplateView.as_view(),
        name='form'
    ),
    path(
        route='list',
        view=UsuarioHtmxListView.as_view(),
        name='list'
    ),
    path(
        route='create',
        view=UsuarioHtmxCreateView.as_view(),
        name='create'
    ),
    path(
        route='update/<int:pk>/',
        view=UsuarioHtmxUpdateView.as_view(),
        name='update'
    ),
    path(
        route='delete/<int:pk>/',
        view=UsuarioHtmxDeleteView.as_view(),
        name='delete'
    ),
    path(
        route='retornar_usuarios/',
        view=RetornarUsuarios.as_view(),
        name='retornar_usuarios'),
]
