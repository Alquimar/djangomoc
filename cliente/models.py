from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    salario = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField()
    filhos = models.IntegerField()
    ativo = models.NullBooleanField()

    def __str__(self):
        return self.nome
