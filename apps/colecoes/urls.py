from django.urls import path
from .views import (ColecaoTemplateView, ColecaoHtmxListView, ColecaoHtmxCreateView,
                    ColecaoHtmxUpdateView, ColecaoHtmxDeleteView, ColecaoHtmxAddItensListView,
                    ColecaoHtmxAddItensCreateView, ItensColecaoTemplateView)


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
        route='form_itens/<int:pk>/',
        view=ItensColecaoTemplateView.as_view(),
        name='form_itens'
    ),
    path(
        route='adicionar_itens_list',
        view=ColecaoHtmxAddItensListView.as_view(),
        name='adicionar_itens_list'
    ),
    path(
        route='adicionar_itens_create',
        view=ColecaoHtmxAddItensCreateView.as_view(),
        name='adicionar_itens_create'
    ),
]
