from django.urls import path

from .views import (PessoaHtmxListView, PessoaHtmxCreateView,
                    PessoaHtmxUpdateView, PessoaHtmxDeleteView,
                    PessoaTemplateView)

app_name = 'pessoa'

urlpatterns = [
    path(
        route='form',
        view=PessoaTemplateView.as_view(),
        name='form'
    ),
    path(
        route='list',
        view=PessoaHtmxListView.as_view(),
        name='list'
    ),
    path(
        route='create',
        view=PessoaHtmxCreateView.as_view(),
        name='create'
    ),
    path(
        route='update/<int:pk>/',
        view=PessoaHtmxUpdateView.as_view(),
        name='update'
    ),
    path(
        route='delete/<int:pk>/',
        view=PessoaHtmxDeleteView.as_view(),
        name='delete'
    )
]
