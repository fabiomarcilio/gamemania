from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages

from apps.itens.models import Item
from apps.itens.forms import ItemModelForm


class ItemTemplateView(TemplateView):
    template_name = 'itens/form.html'


class ItemHtmxListView(SuccessMessageMixin, ListView):
    model = Item
    template_name = 'itens/partials/htmx_item_list.html'
    context_object_name = 'itens'
    paginate_by = 5
    ordering = '-id'


class ItemHtmxCreateView(SuccessMessageMixin, CreateView):
    model = Item
    template_name = 'itens/partials/htmx_item_dados.html'
    form_class = ItemModelForm
    sucess_message = 'Item cadastrado!'
    success_url = 'form'


class ItemHtmxUpdateView(SuccessMessageMixin, UpdateView):
    model = Item
    form_class = ItemModelForm
    template_name = 'itens/partials/htmx_item_dados.html'
    success_message = 'Item alterado!'

    def get_success_url(self):
        return reverse('item:form')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item_id = self.kwargs['pk']
        context['item_id'] = item_id
        item = Item.objects.get(id=item_id)
        form_item = ItemModelForm(initial=item.__dict__)
        context['form'] = form_item
        return context


class ItemHtmxDeleteView(SuccessMessageMixin, DeleteView):
    model = Item
    success_message = 'Item excluído!'
    context_object_name = 'itens'
    template_name = 'itens/partials/htmx_item_list.html'
    success_url = 'form'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, self.success_message)
        response = render(request, self.template_name)
        response['HX-trigger'] = 'hx-list-updated'

        return response
