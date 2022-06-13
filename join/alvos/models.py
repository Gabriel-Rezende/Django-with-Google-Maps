from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Alvo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    latitude = models.DecimalField(
            max_digits=9,
            decimal_places=6,
            validators=[
                MaxValueValidator(90),
                MinValueValidator(-90)
            ])
    longitude = models.DecimalField(
            max_digits=9,
            decimal_places=6,
            validators=[
            MaxValueValidator(180),
            MinValueValidator(-180)
        ])
    data_expiracao = models.DateField()

    class Meta:
        ordering = ['nome']
        verbose_name = 'Alvo'
        verbose_name_plural = 'Alvos'

    def __str__(self):
        return '{}'.format(self.nome)
