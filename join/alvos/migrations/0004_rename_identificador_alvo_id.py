# Generated by Django 3.2.13 on 2022-06-12 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alvos', '0003_alvo_data_expiracao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alvo',
            old_name='identificador',
            new_name='id',
        ),
    ]
