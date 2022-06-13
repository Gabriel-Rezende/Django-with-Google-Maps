from django.test import TestCase
from .models import Alvo

class AlvoTestCase(TestCase):
    def setUp(self):
        self.alvo1 = Alvo.objects.create(nome="Alvo1", latitude=30.5555, longitude=30, data_expiracao='2022-06-20')

    def test_criar_alvo(self):
        alvo = {'nome':'AlvoTeste', 'latitude': '50', 'longitude': '45.5555', 'data_expiracao': '15/06/2022'}
        response = self.client.post('/alvos/adicionar/', alvo)
        self.assertTrue(Alvo.objects.filter(nome='AlvoTeste').exists())

    def test_editar_alvo(self):
        alvo = {
                'nome': 'AlvoNovoNome',
                'latitude': str(self.alvo1.latitude),
                'longitude': str(self.alvo1.longitude),
                'data_expiracao': self.alvo1.data_expiracao
        }
        response = self.client.post(f'/alvos/editar/{self.alvo1.id}/', alvo)
        self.assertTrue(Alvo.objects.get(id=self.alvo1.id).nome == 'AlvoNovoNome')

    def test_excluir_alvo(self):
        response = self.client.post(f'/alvos/excluir/{self.alvo1.id}/')
        self.assertFalse(Alvo.objects.filter(id=self.alvo1.id).exists())


    def test_latitude_longitude_errada(self):
        alvo = {'nome':'AlvoTeste', 'latitude': '91', 'longitude': '-181', 'data_expiracao': '15/06/2022'}
        response = self.client.post('/alvos/adicionar/', alvo)
        self.assertFalse(Alvo.objects.filter(nome='AlvoTeste').exists())
