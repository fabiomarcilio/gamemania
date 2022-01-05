from django.contrib.messages.api import success
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, UpdateView, FormView
from django.views.generic.list import ListView
from apps.usuarios.forms import UsuarioModelForm
from django.contrib.messages.views import SuccessMessageMixin

from apps.usuarios.models import Usuario


class UsuarioTemplateView(TemplateView):
    template_name = 'usuarios/form.html'


class UsuarioHtmxListView(ListView):
    model = Usuario
    template_name = 'usuarios/partials/htmx_usuario_list.html'
    context_object_name = 'usuarios'
    paginate_by = 5
    ordering = '-id'

    # def get_queryset(self, *args, **kwargs):
    #     if self.request.GET.get('usuario_id'):
    #         usuarios = Usuario.objects.filter(
    #             usuario_id=self.request.GET.get('usuario_id')).order_by('-id')
    #         return usuarios


class UsuarioHtmxCreateView(SuccessMessageMixin, CreateView):
    model = Usuario
    template_name = 'usuarios/partials/htmx_usuario_dados.html'
    form_class = UsuarioModelForm
    sucess_message = 'Usuário cadastrado'

    # def get_success_url(self):
    #     return reverse('usuario:index')

    # def form_valid(self, form):
    #     usuario = UsuarioModelForm()
    #     usuario.load_from_dict(form.cleaned_data)
    #     usuario.save()
    #     messages.success(self.request, self.success_message)
    #     context = self.get_context_data(form=form)
    #     context['usuario_id'] = usuario.id
    #     return self.render_to_response(context)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["usuarios"] = Usuario.objects.all().order_by('-id')
    #     return context


class UsuarioHtmxUpdateView(FormView):
    # model = Usuario
    form_class = UsuarioModelForm
    # success_message = 'Usuário alterado!'
    # error_message = 'Falha ao gravar!'
    template_name = 'usuarios/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario_id = self.request.GET.get('usuario_id')
        context['usuario_id'] = usuario_id
        usuario = Usuario(id=usuario_id)
        form_usuario = UsuarioModelForm(initial=usuario.__dict__)
        context['form'] = form_usuario
        return context

    # def get_success_url(self) -> str:
    #     return self.request.META.get('HTTP_REFERER', '/')


class UsuarioHtmxDeleteView(DeleteView):
    model = Usuario
    success_message = 'Usuário excluído!'

    def delete(self, request, *args, **kwargs):
        super(UsuarioHtmxDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('usuario:form')
