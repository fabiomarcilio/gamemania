from django.db import models
from django.db.models.constraints import UniqueConstraint

UFS_SIGLAS = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
]


class Usuario(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False,
                            db_index=True, error_messages={"unique": "Usuário já cadastrado"})
    cpf = models.CharField(max_length=9, blank=True, null=True, error_messages={
                           "unique": "CPF já cadastrado"})
    foto = models.ImageField()
    data_nascimento = models.DateField(blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True,
                             null=True, db_index=True)
    redes_sociais = models.CharField(max_length=255, blank=True, null=True)
    # Endereço:
    cep = models.CharField(max_length=9, blank=True, null=True)
    logradouro = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    uf = models.CharField(
        max_length=2, blank=False, null=False, choices=UFS_SIGLAS, default='SP')
    numero = models.DecimalField(
        max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    constraints = [
        UniqueConstraint(fields=['nome'], name='usuario_nome_unique'),
        UniqueConstraint(fields=['cpf'], name='usuario_cpf_unique'),
        UniqueConstraint(fields=['cep'], name='usuario_cep_unique')
    ]

    def __str__(self) -> str:
        return self.nome
