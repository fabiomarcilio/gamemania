from django.urls import path
from .views import (ColecaoTemplateView, ColecaoHtmxListView, ColecaoHtmxCreateView,
                    ColecaoHtmxUpdateView, ColecaoHtmxDeleteView, ColecaoHtmxAddItensView)


app_name = 'colecao'

urlpatterns = [
    path(
        route='form',
        view=ColecaoTemplateView.as_view(),
        name='form'
    ),
    path(
        route='list',
        view=ColecaoHtmxListView.as_view(),
        name='list'
    ),
    path(
        route='create',
        view=ColecaoHtmxCreateView.as_view(),
        name='create'
    ),
    path(
        route='update/<int:pk>/',
        view=ColecaoHtmxUpdateView.as_view(),
        name='update'
    ),
    path(
        route='delete/<int:pk>/',
        view=ColecaoHtmxDeleteView.as_view(),
        name='delete'
    ),
    path(
        route='adicionar_itens/',
        view=ColecaoHtmxAddItensView.as_view(),
        name='adicionar_itens'
    ),
]
