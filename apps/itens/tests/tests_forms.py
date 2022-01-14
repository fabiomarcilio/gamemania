from django.test import TestCase

from apps.itens.forms import ItemModelForm

# Rodar o teste com o seguinte comando:
# python manage.py test apps.itens.tests.tests_forms


class ItemFormTestCase(TestCase):

    def test_item_form_valido(self):
        form = ItemModelForm(data={
            'nome': 'Mega Drive', 'descricao': 'Versão 1', 'marca': 'Sega', 'modelo': 'V1', 'cor': 'preta'
        })
        self.assertTrue(form.is_valid())

    def test_item_form_invalido(self):
        form = ItemModelForm(data={})
        self.assertFalse(form.is_valid())
