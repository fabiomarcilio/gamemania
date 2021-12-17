from django.contrib.messages.api import success
from django.shortcuts import render
from django.views.generic import CreateView
from apps.usuarios.forms import UsuarioModelForm
from django.contrib.messages.views import SuccessMessageMixin

from apps.usuarios.models import Usuario


class UsuarioListView():
    pass


class UsuarioCreateView(SuccessMessageMixin, CreateView):
    model = Usuario
    template_name = 'usuarios/form.html'
    form_class = UsuarioModelForm
    sucess_message = 'Usuário cadastrado'
