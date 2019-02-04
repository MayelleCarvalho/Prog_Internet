from django.db import models

# Create your models here.

class Endereco(models.Model):
  rua = models.CharField(max_length=100)
  bairro = models.CharField(max_length=100)
  numero = models.IntegerField()
  complemento = models.CharField(max_length=100)
  cep = models.CharField(max_length=10)
  cidade = models.CharField(max_length=100)


class Empresa(models.Model):
  nome = models.CharField(max_length=100)
  cnpj = models.CharField(max_length=18)
  sloga = models.CharField(max_length=200)


class Usuario(models.Model):
  nome_usuario = models.CharField(max_length=20)
  website = models.CharField(max_length=50)
  nome = models.CharField(max_length=20)
  empresa = models.CharField(max_length=200)
  telefone = models.CharField(max_length=200)
  endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, related_name='enderecos')
  email = models.EmailField()


class Post(models.Model):
  body = models.CharField(max_length=200)
  autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='posts')
  titulo = models.CharField(max_length=100)


class Comentario(models.Model):
  body = models.CharField(max_length=500)
  email = models.CharField(max_length=500)
  post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comentarios')
  titulo = models.CharField(max_length=50)


