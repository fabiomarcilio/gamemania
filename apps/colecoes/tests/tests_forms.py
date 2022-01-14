from django.test import TestCase

from apps.colecoes.forms import ColecaoModelForm
from apps.usuarios.models import Usuario

# Rodar o teste com o seguinte comando:
# python manage.py test apps.colecoes.tests.tests_forms


class ColecaoFormTestCase(TestCase):

    def test_colecao_form_valido(self):
        form = ColecaoModelForm(data={
            'nome': 'Sega', 'descricao': 'colecao de portáteis', 'data_inicio': '2021-01-01', 'valor_estimado': '10.000'
        })
        self.assertTrue(form.is_valid())

    def test_colecao_form_invalido(self):
        form = ColecaoModelForm(data={})
        self.assertFalse(form.is_valid())
