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


class Pessoa(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False,
                            db_index=True, error_messages={"unique": "Pessoa já cadastrado"})
    cpf = models.CharField(max_length=11, blank=True, null=True, error_messages={
                           "unique": "CPF já cadastrado"})
    foto = models.ImageField(blank=True, null=True,
                             upload_to='pessoas')
    data_nascimento = models.DateField(blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True,
                             null=True, db_index=True, unique=True)
    redes_sociais = models.CharField(max_length=255, blank=True, null=True)
    # Endereço:
    cep = models.CharField(max_length=9, blank=True, null=True)
    logradouro = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    uf = models.CharField(
        max_length=2, blank=True, null=False, choices=UFS_SIGLAS, default='SP')
    numero = models.DecimalField(
        max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        db_table = 'pessoas'
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    constraints = [
        UniqueConstraint(fields=['nome'], name='pessoa_nome_unique'),
        UniqueConstraint(fields=['cpf'], name='pessoa_cpf_unique'),
        UniqueConstraint(fields=['cep'], name='pessoa_cep_unique')
    ]

    def __str__(self) -> str:
        return self.nome
