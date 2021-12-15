from django.db import models
from django.db.models.constraints import UniqueConstraint


class Usuario(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False,
                            db_index=True, error_messages={"unique": "Usuário já cadastrado"})
    cpf = models.CharField(max_length=9, blank=True, null=True, error_messages={
                           "unique": "CPF já cadastrado"})
    foto = models.ImageField()
    data_nascimento = models.DateField(blank=True, null=True)
    telefone = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    redes_sociais = models.CharField(blank=True, null=True)
    # Endereço:
    cep = models.CharField(max_length=9, blank=True, null=True)
    logradouro = models.CharField(max_length=55, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    numero = models.DecimalField(
        max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    constraints = [
        UniqueConstraint(fields=['nome'], name='usuario_nome_unique'),
        UniqueConstraint(fields=['cpf'], name='usuario_cpf_unique')
    ]

    def __str__(self) -> str:
        return self.nome
