# Generated by Django 3.1.1 on 2022-01-26 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0001_initial'),
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
                ('foto', models.ImageField(blank=True, null=True, upload_to='colecoes')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pessoa', to='pessoas.pessoa')),
            ],
            options={
                'verbose_name': 'Coleção',
                'verbose_name_plural': 'Coleções',
                'db_table': 'colecoes',
            },
        ),
    ]
