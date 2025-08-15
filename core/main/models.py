from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    SEXO = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Outro'),
    ]

    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=64)
    sobrenome = models.CharField(max_length=64)
    sexo = models.CharField(choices=SEXO, max_length=9)
    rua = models.CharField(max_length=64)
    numero = models.CharField(max_length=8)
    bairro = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

class RegistroSaude(models.Model):
    data_registro = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    glicemia = models.IntegerField(null=True, blank=True)
    pressao_sistolica = models.IntegerField(null=True, blank=True)
    pressao_diastolica = models.IntegerField(null=True, blank=True)
    peso = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    frequencia_cardiaca = models.IntegerField(null=True, blank=True)

class Consulta(models.Model):
    ESPECIALIDADE = [
        ('cardiologista', 'Cardiologista'),
        ('clinico-geral', 'Clínico Geral'),
        ('geriatra', 'Geriatra'),
        ('cargiologista', 'Cardiolgista'),
        ('Ortopedista', 'Ortopedista'),
        ('endocrinologista', 'Endocrinologista'),
        ('reumatologista', 'Reumatologista'),
        ('outro', 'Outro'),
    ]

    MEDICO = [
        ('dr-joao', 'Dr. João Silva'),
        ('dra-maria', 'Dra. Maria Santos'),
        ('dr-davi', 'Dr. Davi Borges'),
        ('dra-ana', 'Dra. Ana Almeida'),
        ('dr-miguel', 'Dr. Miguel Soares'),
        ('dra-sophia', 'Dra. Sophia Rocha'),
        ('dr-gabriel', 'Dr. Gabriel Santana'),
        ('dra-alice', 'Dra. Alice de Moraes'),
    ]

    HORA = [
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
    ]

    solicitante = models.ForeignKey(User, on_delete=models.CASCADE)
    data_solicitacao = models.DateTimeField(auto_now=True)
    titulo = models.CharField(max_length=64)
    especialidade  = models.CharField(choices=ESPECIALIDADE)
    medico = models.CharField(choices=MEDICO)
    data_atendimento = models.DateField()
    hora_atendimento = models.CharField(choices=HORA, max_length=5)
    observacao = models.TextField(null=True, blank=True)