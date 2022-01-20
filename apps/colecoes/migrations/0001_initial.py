# Generated by Django 3.1.1 on 2022-01-19 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colecao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=255, null=True)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('valor_estimado', models.CharField(blank=True, max_length=255, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='media/usuarios')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuario', to='usuarios.usuario')),
            ],
            options={
                'verbose_name': 'Coleção',
                'verbose_name_plural': 'Coleções',
                'db_table': 'colecoes',
            },
        ),
    ]
