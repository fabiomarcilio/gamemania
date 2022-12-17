from django.shortcuts import render
from django.urls import reverse
from dal import autocomplete
from django.contrib import messages
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView
from apps.usuarios.forms import UsuarioModelForm, UsuarioFiltroIndexForm
from django.contrib.messages.views import SuccessMessageMixin

from apps.usuarios.models import CustomUsuario


class UsuarioTemplateView(SuccessMessageMixin, TemplateView):
    template_name = 'usuarios/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = CustomUsuario.object.filter(
            id=self.request.user.id)
        context["usuario"] = usuario
        return context


class UsuarioHtmxListView(SuccessMessageMixin, ListView):
    model = CustomUsuario
    template_name = 'usuarios/partials/htmx_usuario_list.html'
    context_object_name = 'usuarios'
    paginate_by = 5
    ordering = '-id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UsuarioFiltroIndexForm()
        return context


class UsuarioHtmxCreateView(SuccessMessageMixin, CreateView):
    model = CustomUsuario
    template_name = 'usuarios/partials/htmx_usuario_dados.html'
    form_class = UsuarioModelForm
    sucess_message = 'Usuário cadastrado'
    success_url = 'form'


class UsuarioHtmxUpdateView(SuccessMessageMixin, UpdateView):
    model = CustomUsuario
    form_class = UsuarioModelForm
    template_name = 'usuarios/partials/htmx_usuario_dados.html'
    success_message = 'Usuario alterado!'

    def get_success_url(self):
        return reverse('usuario:form')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario_id = self.kwargs['pk']
        context['usuario_id'] = usuario_id
        usuario = CustomUsuario.objects.get(id=usuario_id)
        form_usuario = UsuarioModelForm(initial=usuario.__dict__)
        context['usuario'] = usuario
        context['form'] = form_usuario
        return context


class UsuarioHtmxDeleteView(SuccessMessageMixin, DeleteView):
    model = CustomUsuario
    success_message = 'Usuário excluído!'
    context_object_name = 'usuarios'
    template_name = 'usuarios/partials/htmx_usuario_list.html'
    success_url = 'form'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, self.success_message)
        response = render(request, self.template_name)
        response['HX-trigger'] = 'hx-list-updated'

        return response


class RetornarUsuarios(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return CustomUsuario.objects.none()

        qs = CustomUsuario.objects.all()

        if self.q:
            qs = qs.filter(first_name__istartswith=self.q)

        return qs
