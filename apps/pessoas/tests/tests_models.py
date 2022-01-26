from django.test import TestCase
from apps.pessoas.models import Pessoa

# Rodar o teste com o seguinte comando:
# python manage.py test apps.pessoas.tests.tests_models


class PessoaTestCase(TestCase):
    def setUp(self):
        Pessoa.objects.create(
            nome='Fabio', cpf='29805758010', data_nascimento='1982-02-03',
            telefone='11997861111', email='fabiomar@mail.com', redes_sociais='fabiomarc',
            cep='12400370', logradouro='Rua dos expedicionários', bairro='Centro', cidade='Pindamonhangaba',
            uf='SP', numero='123'
        )

    def test_cadastro_pessoa(self):
        '''Testa se o pessoa foi cadastrado corretamente no modelo'''
        pessoa = Pessoa.objects.all().count()
        self.assertEqual(pessoa, 1)
        self.assertNotEqual(pessoa, 0)
