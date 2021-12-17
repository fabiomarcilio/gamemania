from django.urls import path

from .views import UsuarioListView, UsuarioCreateView

app_name = 'usuario'

urlpatterns = [
    path(
        route='',
        view=UsuarioListView,
        name='list'
    ),
    path(
        route='index',
        view=UsuarioCreateView.as_view(),
        name='index'
    )
]
