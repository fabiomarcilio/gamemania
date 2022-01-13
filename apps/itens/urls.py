from django.urls import path

from apps.itens.views import (ItemTemplateView, ItemHtmxCreateView, ItemHtmxListView,
                              ItemHtmxUpdateView, ItemHtmxDeleteView)

app_name = 'item'

urlpatterns = [
    path(
        route='form',
        view=ItemTemplateView.as_view(),
        name='form'
    ),
    path(
        route='list',
        view=ItemHtmxListView.as_view(),
        name='list'
    ),
    path(
        route='create',
        view=ItemHtmxCreateView.as_view(),
        name='create'
    ),
    path(
        route='update/<int:pk>/',
        view=ItemHtmxUpdateView.as_view(),
        name='update'
    ),
    path(
        route='delete/<int:pk>/',
        view=ItemHtmxDeleteView.as_view(),
        name='delete'
    ),
]
