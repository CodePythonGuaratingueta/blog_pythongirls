from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=60)
    conteudo = models.TextField()
    data_criacao = models.DateField()
    data_modificacao = models.DateField()
    autor_id = models.ForeignKey('blog.Autor')
    categoria_id = models.ForeignKey('blog.Categoria')
    tag_id = models.ForeignKey('blog.Tag')


class Autor(models.Model):
    user_id = models.OneToOneField(User)
    descricao = models.TextField()
    foto = models.CharField(max_length=255)


class Tag(models.Model):
    nome = models.CharField(max_length=60)
    data_criacao = models.DateField()
    data_modificacao = models.DateField()


class Categoria(models.Model):
    nome = models.CharField(max_length=60)
    data_criacao = models.DateField()
    data_modificacao = models.DateField()


class Banner(models.Model):
    foto = models.CharField(max_length=255)
    ordem = models.IntegerField()
    texto = models.TextField()
    link = models.CharField(max_length=255)