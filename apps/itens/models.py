from django.db import models
from apps.colecoes.models import Colecao

from apps.usuarios.models import CustomUsuario


class Item(models.Model):
    colecao = models.ForeignKey(
        Colecao, related_name='colecoes', blank=False, null=False, on_delete=models.PROTECT)
    usuario = models.ForeignKey(
        CustomUsuario, related_name='usuarios', blank=False, null=False, on_delete=models.PROTECT)
    nome_item = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    cor = models.CharField(max_length=255, blank=True, null=True)
    foto = models.ImageField(blank=True, null=True,
                             upload_to='itens')
    data_compra = models.DateField(blank=True, null=True)
    valor_pago = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    valor_venda = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    estado_item = models.CharField(max_length=100, blank=True, null=True)
    disponivel_venda = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'itens'
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self) -> str:
        return self.nome

