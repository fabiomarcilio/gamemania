from django.test import TestCase
from apps.usuarios.models import Usuario

# Rodar o teste com o seguinte comando:
# python manage.py test apps.usuarios.tests


class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(
            nome='Fabio', cpf='29805758010', data_nascimento='1982-02-03',
            telefone='11997861111', email='fabiomar@mail.com', redes_sociais='fabiomarc',
            cep='12400370', logradouro='Rua dos expedicionários', bairro='Centro', cidade='Pindamonhangaba',
            uf='SP', numero='123'
        )

    def test_cadastro_usuario(self):
        '''Testa se o usuário foi cadastrado corretamente no modelo'''
        usuario = Usuario.objects.all().count()
        self.assertEqual(usuario, 1)
        self.assertNotEqual(usuario, 0)
