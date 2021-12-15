from django.db import models
from django.db.models.deletion import PROTECT

from apps.itens.models import ItemUsuario


class Colecao(models.Model):

    item_usuario = models.ForeignKey(
        ItemUsuario, related_name='itens_usuario', blank=True, null=True, on_delete=PROTECT)
    nome = models.CharField(max_length=55, blank=True, null=True)
    descricao = models.CharField(max_length=55, blank=True, null=True)
    foto = models.ImageField()

    class Meta:
        db_table = 'colecoes'
        verbose_name = 'Coleção'
        verbose_name_plural = 'Coleções'
