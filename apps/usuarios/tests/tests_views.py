from django.test import TestCase
from django.urls import reverse

# Comando para rodar o teste:
# python manage.py test apps.pessoas.tests.tests_views


class PessoaViewTestCase(TestCase):
    # Verifica se o status de retorno da view é 200
    def test_status_code_200(self):
        # client é utilizado para simular uma requisição
        response = self.client.get(reverse('pessoa:form'))
        self.assertEqual(response.status_code, 200)
    # Testa se o template é chamado corretamente.

    def test_template_usado(self):
        response = self.client.get(reverse('pessoa:form'))
        self.assertTemplateUsed(response, 'pessoas/form.html')