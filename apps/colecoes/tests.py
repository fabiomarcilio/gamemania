from django.test import TestCase
from apps.colecoes.models import Colecao
from apps.usuarios.models import Usuario

# Rodar o teste com o seguinte comando:
# python manage.py test apps.colecoes.tests


class ColecaoTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(
            nome='Fabio', cpf='29805758010', data_nascimento='1982-02-03',
            telefone='11997861111', email='fabiomar@hotmail.com', redes_sociais='fabiomarcilio',
            cep='12400370', logradouro='Rua dos expedicionários', bairro='Centro', cidade='Pindamonhangaba',
            uf='SP', numero='123'
        )

        Colecao.objects.create(
            usuario_id='1', nome='Sega', descricao='colecao de portáteis', data_inicio='2021-01-01', valor_estimado='10.000'
        )

    def test_cadastro_colecao(self):
        '''Testa se o item foi cadastrado corretamente no modelo'''
        colecao = Colecao.objects.all().count()
        self.assertEqual(colecao, 1)
        self.assertNotEqual(colecao, 0)
