# Generated by Django 4.0.1 on 2022-01-18 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0004_alter_anuncio_codigo_da_empresa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='Codigo_da_Empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nome', to='marketing.empresa'),
        ),
    ]