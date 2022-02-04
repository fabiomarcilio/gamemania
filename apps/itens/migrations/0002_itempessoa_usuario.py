# Generated by Django 3.1.1 on 2022-01-27 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itempessoa',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pessoas', to=settings.AUTH_USER_MODEL),
        ),
    ]