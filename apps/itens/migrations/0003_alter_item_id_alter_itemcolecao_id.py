# Generated by Django 4.0.3 on 2022-12-11 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0002_auto_20220215_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='itemcolecao',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
