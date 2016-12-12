# coding: utf-8
from django.db import models

class DadosPessoais(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    adress = models.CharField(verbose_name='Endereço', max_length=100)
    city = models.CharField(verbose_name='Cidade', max_length=100)
    cep = models.CharField(verbose_name='Cep', max_length=100)
    fhone = models.CharField(verbose_name='Telefone', max_length=20)
    mobile = models.CharField(verbose_name='Celular', max_length=20)

    about = models.TextField(max_length=255, verbose_name='sobre')
    data_nascimento = models.CharField(default='13 de julho de 1964', max_length=100, verbose_name='Data Nascimento')
    email = models.EmailField(verbose_name='Email')

    conhecimentos = models.TextField('Conhecimentos')
    github = models.CharField(default='http://github.com/scarmarcos', max_length=100)
    corrent_position = models.CharField(verbose_name='Cargo', max_length=100)
    empresa = models.CharField(verbose_name='Empresa', max_length=100)

    def __str__(self):
        return senf.name

    class Mete:
        verbose_name = 'Dados Pessoais'
        verbose_name = 'Dados Pessoais'
