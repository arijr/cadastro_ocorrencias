from django.db import models

# Create your models here.

class Ocorrencia(models.Model):

    def __str__(self):
        return self.descricao

    endereco= models.ForeignKey('Endereco',on_delete = models.CASCADE)
    solicitante = models.ForeignKey('Solicitante', on_delete = models.CASCADE)
    tipo = models.ForeignKey('TipoOcorrencia',on_delete = models.DO_NOTHING)

    data = models.DateField(auto_now_add=True)
    motivo =  models.CharField(max_length = 255)
    descricao = models.CharField(max_length = 255)

class Endereco(models.Model):

    def __str__(self):
        return self.rua

    rua = models.CharField(max_length = 255)
    cep = models.CharField(max_length = 12)
    numero = models.DecimalField(decimal_places = 0, max_digits = 12)
    bairro = models.CharField(max_length = 255)
    cidade = models.CharField(max_length = 255)
    estado = models.CharField(max_length = 255)


class Solicitante(models.Model):

    def __str__(self):
        return self.nome

    nome = models.CharField(max_length = 20)
    telefone = models.CharField(max_length = 12)
    cpf = models.DecimalField(decimal_places = 4, max_digits = 12)
    nis = models.DecimalField(decimal_places = 4, max_digits = 12)
    rg = models.DecimalField(decimal_places = 3, max_digits = 8)


class TipoOcorrencia(models.Model):

    def __str__(self):
        return self.tipo

    tipo = models.CharField(max_length = 30)
