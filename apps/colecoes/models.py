from django.db import models
from django.db.models.deletion import PROTECT

from apps.itens.models import ItemUsuario
from apps.usuarios.models import Usuario


class Colecao(models.Model):

    usuario = models.ForeignKey(
        Usuario, related_name='usuario', blank=False, null=False, on_delete=PROTECT)
    nome = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    data_inicio = models.DateField(blank=True, null=True)
    valor_estimado = models.CharField(max_length=255, blank=True, null=True)
    foto = models.ImageField(blank=True, null=True,
                             upload_to='usuarios')

    class Meta:
        db_table = 'colecoes'
        verbose_name = 'Coleção'
        verbose_name_plural = 'Coleções'
