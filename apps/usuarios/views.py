from django.contrib.messages.api import success
from django.shortcuts import render
from django.urls import reverse
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

    def get_success_url(self):
        return reverse('usuario:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuarios"] = Usuario.objects.all().order_by('-id')
        return context
