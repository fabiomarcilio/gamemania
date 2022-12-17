from django.urls import path
from apps.anuncios.views import AnuncioListView, AnuncioTemplateView


app_name = 'anuncio'

urlpatterns = [
    path(
        route='form',
        view=AnuncioTemplateView.as_view(),
        name='form'
    ),
    path(
        route='list',
        view=AnuncioListView.as_view(),
        name='list'
    ),
]