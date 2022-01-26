from django.db import models

from apps.pessoas.models import Pessoa


class Item(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    cor = models.CharField(max_length=255, blank=True, null=True)
    foto = models.ImageField(blank=True, null=True,
                             upload_to='itens')

    class Meta:
        db_table = 'itens'
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self) -> str:
        return self.nome


class ItemPessoa(models.Model):
    item = models.ForeignKey(Item, related_name='itens',
                             blank=True, null=True, on_delete=models.PROTECT)
    pessoa = models.ForeignKey(
        Pessoa, related_name='pessoas', blank=True, null=True, on_delete=models.PROTECT)
    foto = models.ImageField()
    data_compra = models.DateField(blank=True, null=True)
    valor_pago = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    valor_venda = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    estado_item = models.CharField(max_length=100, blank=True, null=True)
    disponivel_venda = models.BooleanField()

    class Meta:
        db_table = 'itens_pessoa'
        verbose_name = 'Item_pessoa'
        verbose_name_plural = 'Itens_pessoa'

    def __str__(self) -> str:
        return self.item_pessoa
