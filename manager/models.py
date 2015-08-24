from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=False)
    sobrenome = models.CharField(max_length=200, null=False)
    telefone = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200)
    data_cadastro = models.DateTimeField(default=timezone.now, null=False)

    def salvar(self):
        self.data_cadastro = timezone.now()
        self.save()

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=200, null=False)
    sobrenome = models.CharField(max_length=200, null=False)
    telefone = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200)
    data_admissao = models.DateTimeField( default=timezone.now, null=False)
    data_demissao = models.DateTimeField(blank=True, null=True)

    def salvar(self):
        self.data_admissao = timezone.now()
        self.save()

    def __str__(self):
        return self.nome

class Historico(models.Model):
    cliente = models.ForeignKey(Cliente)
    funcionario = models.ForeignKey(Funcionario)
    data_chamado = models.DateTimeField(default=timezone.now, null=False)
    data_realizacao = models.DateTimeField(blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField()

    def salvar(self):
        self.data_chamado = timezone.now()
        self.save()

    def ident(self):
        ident = str(self.id)
        return ident
    ident.short_description = 'ID'

    def __str__(self):
        ident = str(self.id)
        return ident


class Servico(models.Model):
    historico = models.ForeignKey(Historico)
    nome = models.CharField(max_length=200, null=False)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome