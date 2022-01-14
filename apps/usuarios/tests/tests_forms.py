from django.test import TestCase

from apps.usuarios.forms import UsuarioModelForm

# Rodar o teste com o seguinte comando:
# python manage.py test apps.usuarios.tests.tests_forms


class UsuarioFormTestCase(TestCase):

    def test_usuario_form_valido(self):
        form = UsuarioModelForm(data={
            'nome': 'Fabio', 'cpf': '29805758010', 'data_nascimento': '1982-02-03',
            'telefone': '11997861111', 'email': 'fabiomar@mail.com', 'redes_sociais': 'fabiomarc',
            'cep': '12400370', 'logradouro': 'Rua dos expedicionários', 'bairro': 'Centro', 'cidade': 'Pindamonhangaba',
            'uf': 'SP', 'numero': '123'
        })
        self.assertTrue(form.is_valid())

    def test_usuario_form_invalido(self):
        form = UsuarioModelForm(data={})
        self.assertFalse(form.is_valid())
