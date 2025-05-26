from django.db import models

from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50, unique=True)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Laboratorio(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    capacidade = models.IntegerField()

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    data_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservas')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='reservas')
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='reservas')

    def __str__(self):
        return f'Reserva {self.id} - {self.data_reserva}'
