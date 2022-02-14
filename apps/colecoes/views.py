from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin

from apps.colecoes.forms import ColecaoModelForm

from .models import Colecao


class ColecaoTemplateView(SuccessMessageMixin, TemplateView):
    template_name = 'colecoes/form.html'


class ColecaoHtmxListView(SuccessMessageMixin, ListView):
    model = Colecao
    template_name = 'colecoes/partials/htmx_colecao_list.html'
    context_object_name = 'colecoes'
    paginate_by = 5
    ordering = '-id'

    def get_context_data(self, **kwargs):
        response = super().get_context_data(**kwargs)
        usuario = self.request.user
        colecao = Colecao.objects.filter(usuario=usuario.id)
        response["colecoes"] = colecao
        return response


class ColecaoHtmxCreateView(SuccessMessageMixin, CreateView):
    model = Colecao
    template_name = 'colecoes/partials/htmx_colecao_dados.html'
    form_class = ColecaoModelForm
    sucess_message = 'Coleção cadastrada!'
    success_url = 'form'

    def form_valid(self, form):
        user = self.request.user
        form.instance.usuario_id = user.id
        form.instance.id = user.id
        return super().form_valid(form)


class ColecaoHtmxUpdateView(SuccessMessageMixin, UpdateView):
    model = Colecao
    form_class = ColecaoModelForm
    template_name = 'colecoes/partials/htmx_colecao_dados.html'
    success_message = 'Coleção alterada!'

    def get_success_url(self):
        return reverse('colecao:form')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        colecao_id = self.kwargs['pk']
        context['colecao_id'] = colecao_id
        colecao = Colecao.objects.get(id=colecao_id)
        form_colecao = ColecaoModelForm(initial=colecao.__dict__)
        context['colecao'] = colecao
        context['form'] = form_colecao
        return context


class ColecaoHtmxDeleteView(SuccessMessageMixin, DeleteView):
    model = Colecao
    success_message = 'Coleção excluída!'
    context_object_name = 'colecoes'
    template_name = 'colecoes/partials/htmx_colecao_list.html'
    success_url = 'form'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, self.success_message)
        response = render(request, self.template_name)
        response['HX-trigger'] = 'hx-list-updated'
        return response
