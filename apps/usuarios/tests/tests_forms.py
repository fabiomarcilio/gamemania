from django.test import TestCase

from apps.pessoas.forms import PessoaModelForm

# Rodar o teste com o seguinte comando:
# python manage.py test apps.pessoas.tests.tests_forms


class PessoaFormTestCase(TestCase):

    def test_pessoa_form_valido(self):
        form = PessoaModelForm(data={
            'nome': 'Fabio', 'cpf': '29805758010', 'data_nascimento': '1982-02-03',
            'telefone': '11997861111', 'email': 'fabiomar@mail.com', 'redes_sociais': 'fabiomarc',
            'cep': '12400370', 'logradouro': 'Rua dos expedicionários', 'bairro': 'Centro', 'cidade': 'Pindamonhangaba',
            'uf': 'SP', 'numero': '123'
        })
        self.assertTrue(form.is_valid())

    def test_pessoa_form_invalido(self):
        form = PessoaModelForm(data={})
        self.assertFalse(form.is_valid())
