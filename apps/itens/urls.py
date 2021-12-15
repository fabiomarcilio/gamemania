from django.urls import path

from apps.itens.views import ItensListView


urlpatterns = [
    path(route='',
         view=ItensListView,
         name='itens'),
]
