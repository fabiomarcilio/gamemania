from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView
from apps.pessoas.forms import PessoaModelForm
from django.contrib.messages.views import SuccessMessageMixin

from apps.pessoas.models import Pessoa


class PessoaTemplateView(SuccessMessageMixin, TemplateView):
    template_name = 'pessoas/form.html'


class PessoaHtmxListView(SuccessMessageMixin, ListView):
    model = Pessoa
    template_name = 'pessoas/partials/htmx_pessoa_list.html'
    context_object_name = 'pessoas'
    paginate_by = 5
    ordering = '-id'


class PessoaHtmxCreateView(SuccessMessageMixin, CreateView):
    model = Pessoa
    template_name = 'pessoas/partials/htmx_pessoa_dados.html'
    form_class = PessoaModelForm
    sucess_message = 'Usuário cadastrado'
    success_url = 'form'

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response


class PessoaHtmxUpdateView(SuccessMessageMixin, UpdateView):
    model = Pessoa
    form_class = PessoaModelForm
    template_name = 'pessoas/partials/htmx_pessoa_dados.html'
    success_message = 'Pessoa alterado!'

    def get_success_url(self):
        return reverse('pessoa:form')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pessoa_id = self.kwargs['pk']
        context['pessoa_id'] = pessoa_id
        pessoa = Pessoa.objects.get(id=pessoa_id)
        form_pessoa = PessoaModelForm(initial=pessoa.__dict__)
        context['pessoa'] = pessoa
        context['form'] = form_pessoa
        return context


class PessoaHtmxDeleteView(SuccessMessageMixin, DeleteView):
    model = Pessoa
    success_message = 'Pessoa excluído!'
    context_object_name = 'pessoas'
    template_name = 'pessoas/partials/htmx_pessoa_list.html'
    success_url = 'form'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, self.success_message)
        response = render(request, self.template_name)
        response['HX-trigger'] = 'hx-list-updated'

        return response
