# Generated by Django 4.0.1 on 2022-01-18 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0007_alter_anuncio_valor_do_anuncio'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='Instagram',
            field=models.URLField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='Site',
            field=models.URLField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='Instagram',
            field=models.URLField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='Responsavel',
            field=models.CharField(max_length=50, null=True),
        ),
    ]