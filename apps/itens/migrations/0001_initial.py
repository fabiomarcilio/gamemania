# Generated by Django 3.1.1 on 2022-01-25 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('marca', models.CharField(blank=True, max_length=255, null=True)),
                ('modelo', models.CharField(blank=True, max_length=255, null=True)),
                ('cor', models.CharField(blank=True, max_length=255, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='itens')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
                'db_table': 'itens',
            },
        ),
        migrations.CreateModel(
            name='ItemPessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='')),
                ('data_compra', models.DateField(blank=True, null=True)),
                ('valor_pago', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('valor_venda', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('estado_item', models.CharField(blank=True, max_length=100, null=True)),
                ('disponivel_venda', models.BooleanField()),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='itens', to='itens.item')),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pessoas', to='pessoas.pessoa')),
            ],
            options={
                'verbose_name': 'Item_pessoa',
                'verbose_name_plural': 'Itens_pessoa',
                'db_table': 'itens_pessoa',
            },
        ),
    ]
