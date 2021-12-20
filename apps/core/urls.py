from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path(
        route='',
        view=views.dashboard,
        name='index',
    )
]
