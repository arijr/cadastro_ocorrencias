# Generated by Django 2.0.5 on 2018-06-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencias', '0002_auto_20180603_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.DecimalField(decimal_places=0, max_digits=12),
        ),
    ]
