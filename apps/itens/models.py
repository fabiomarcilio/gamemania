from django.db import models

from apps.usuarios.models import Usuario


class Item(models.Model):
    nome = models.CharField(max_length=55, blank=False, null=False)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    marca = models.CharField(max_length=15, blank=True, null=True)
    modelo = models.CharField(max_length=15, blank=True, null=True)
    cor = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'itens'
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self) -> str:
        return self.nome


class ItemUsuario(models.Model):
    item = models.ForeignKey(Item, related_name='itens',
                             blank=True, null=True, on_delete=models.PROTECT)
    usuario = models.ForeignKey(
        Usuario, related_name='usuarios', blank=True, null=True, on_delete=models.PROTECT)
    foto = models.ImageField()
    data_compra = models.DateField(blank=True, null=True)
    valor_pago = models.DecimalField(blank=True, null=True)
    valor_venda = models.DecimalField(blank=True, null=True)
    estado_item = models.CharField(max_length=100, blank=True, null=True)
    disponivel_venda = models.BooleanField()

    class Meta:
        db_table = 'itens_usuario'
        verbose_name = 'Item_usuario'
        verbose_name_plural = 'Itens_usuario'

    def __str__(self) -> str:
        return self.item_usuario
