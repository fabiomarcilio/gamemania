from django.test import TestCase
from apps.itens.models import Item

# Rodar o teste com o seguinte comando:
# python manage.py test apps.itens.tests


class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(
            nome='Mega Drive', descricao='Versão 1', marca='Sega', modelo='V1', cor='preta'
        )

    def test_cadastro_item(self):
        '''Testa se o item foi cadastrado corretamente no modelo'''
        item = Item.objects.all().count()
        self.assertEqual(item, 1)
        self.assertNotEqual(item, 0)
