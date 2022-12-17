# from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from apps.itens.models import Item


class AnuncioTemplateView(SuccessMessageMixin, TemplateView):
    template_name = 'anuncios/form.html'


class AnuncioListView(SuccessMessageMixin, ListView):
    model = Item
    template_name = 'anuncios/partials/htmx_anuncio_list.html'
    context_object_name = 'anuncios'
    paginate_by = 5
    ordering = '-id'

    def get_context_data(self, **kwargs):
        response = super().get_context_data(**kwargs)
        response["anuncios"] = Item.objects.filter(disponivel_venda=True)
        return response
