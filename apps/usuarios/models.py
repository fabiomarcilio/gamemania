from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
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


class UsuarioManager(BaseUserManager):
    # Necessário para informar ao django que o banco sera criado.
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisar ter is_staff=True')

        return self.create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):

    first_name = models.CharField(max_length=255, blank=False, null=False,
                                  db_index=True, error_messages={"unique": "Pessoa já cadastrado"})
    last_name = models.CharField(
        max_length=255, blank=False, null=False, db_index=True)
    cpf = models.CharField(max_length=14, blank=True, null=True, error_messages={
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

    # email = models.CharField(max_length=255, blank=True,
    #                          null=True, db_index=True, unique=True)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    constraints = [
        UniqueConstraint(fields=['first_name'], name='pessoa_nome_unique'),
        UniqueConstraint(fields=['cpf'], name='pessoa_cpf_unique'),
        UniqueConstraint(fields=['cep'], name='pessoa_cep_unique')
    ]

    def __str__(self) -> str:
        return self.first_name

    # def __str__(self) -> str:
    #     return self.email

    # Necessário especificar para o UserManager customizado funcionar e não o do django
    object = UsuarioManager()
