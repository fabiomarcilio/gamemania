from django.db import models
from django.db.models.deletion import PROTECT

from apps.itens.models import ItemPessoa
from apps.pessoas.models import Pessoa


class Colecao(models.Model):

    pessoa = models.ForeignKey(
        Pessoa, related_name='pessoa', blank=False, null=False, on_delete=PROTECT)
    nome = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    data_inicio = models.DateField(blank=True, null=True)
    valor_estimado = models.CharField(max_length=255, blank=True, null=True)
    foto = models.ImageField(blank=True, null=True,
                             upload_to='colecoes')

    class Meta:
        db_table = 'colecoes'
        verbose_name = 'Coleção'
        verbose_name_plural = 'Coleções'
