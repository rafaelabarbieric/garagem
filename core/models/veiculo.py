from django.db import models

from .acessorio import Acessorio
from .modelo import Modelo
from .cor import Cor

class Veiculo(models.Model):
    ano = models.IntegerField(null=True, default=(0))
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=(0))
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculo", null=True, blank=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculo", null=True, blank=True)
    acessorio = models.ManyToManyField(Acessorio, related_name='livros', blank=True)

    def __str__(self):
        return f"{self.id} {self.modelo} {self.cor} {self.ano}"