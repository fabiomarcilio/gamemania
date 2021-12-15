from django.urls import path
from apps.colecoes import views

urlpatterns = [
    path(
        route='',
        view=views.ColecoesListView,
        name='index'),
]
