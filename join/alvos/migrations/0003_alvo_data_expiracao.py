# Generated by Django 3.2.13 on 2022-06-12 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alvos', '0002_auto_20220611_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='alvo',
            name='data_expiracao',
            field=models.DateField(default='2022-06-11'),
            preserve_default=False,
        ),
    ]
