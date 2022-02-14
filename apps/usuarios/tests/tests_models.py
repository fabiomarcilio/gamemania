from django.test import TestCase
from apps.usuarios.models import CustomUsuario

# Rodar o teste com o seguinte comando:
# python manage.py test apps.usuarios.tests.tests_models


class UsuarioTestCase(TestCase):
    def setUp(self):
        CustomUsuario.objects.create(
            first_name='Fabio', last_name='Marcílio', cpf='29805758010', data_nascimento='1982-02-03',
            telefone='11997861111', email='fabiomar@mail.com', redes_sociais='fabiomarc',
            cep='12400370', logradouro='Rua dos expedicionários', bairro='Centro', cidade='Pindamonhangaba',
            uf='SP', numero='123'
        )

    def test_cadastro_usuario(self):
        '''Testa se o pessoa foi cadastrado corretamente no modelo'''
        usuario = CustomUsuario.objects.all().count()
        self.assertEqual(usuario, 1)
        self.assertNotEqual(usuario, 0)
