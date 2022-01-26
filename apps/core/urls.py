
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path(
        route='',
        view=views.Dashboard.as_view(),
        name='index',
    ),
    # path('contas/', include('django.contrib.auth.urls')),
]
