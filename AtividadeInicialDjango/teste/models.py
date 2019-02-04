from django.db import models


class Pessoa(models.Model):
    TAM_ROUPA = (
        ('P', 'PEQUENA'),
        ('M', 'MEDIA'),
        ('G', 'GRANDE'),
    )
    primeiro_nome = models.CharField(max_length=60)
    tam_roupa = models.CharField(max_length=1, choices=TAM_ROUPA )


class Blog(models.Model):
    nome = models.CharField(max_length=60)


class Entry(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.CharField(max_length=500)
    data_pub = models.DateField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


class Fruta(models.Model):
    nome = models.CharField(max_length=10, primary_key=True)

class Fabricante(models.Model):
    nome = models.CharField(max_length=40)

class Carro(models.Model):
    nome = models.CharField(max_length=40)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, related_name='carros')


class Cobertura(models.Model):
    descricao = models.CharField(max_length=20)


class Pizza(models.Model):
    nome = models.CharField(max_length=40)
    cobertura = models.ManyToManyField(Cobertura)


class CPF(models.Model):
    numero = models.CharField(max_length=9)

class PessoaFisica(models.Model):
    nome = models.CharField(max_length=40)
    cpf = models.OneToOneField(CPF, on_delete=models.CASCADE, related_name='pessoa_fisica')

class Pessoa2(models.Model):
    nome = models.CharField(max_length=40)

class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    membro = models.ManyToManyField(Pessoa2, through='Associacao')

class Associacao(models.Model):
    pessoa = models.ForeignKey(Pessoa2, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=100)

class Usuario(models.Model):
    email = models.CharField(max_length=60)
    data_nasc = models.DateField()
    senha = models.CharField(max_length=30)

class Perfil(models.Model):
    nome = models.CharField(max_length=60)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='perfis')

class Postagem(models.Model):
    texto = models.CharField(max_length=500)
    data = models.DateField()
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='posts')

class Comentario(models.Model):
    texto = models.CharField(max_length=250)
    data = models.DateField()
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)



class Reacao(models.Model):
    tipo = models.CharField(max_length=10)
    peso = models.IntegerField()

class PostReacao(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name= 'reacoes_post')
    reacao = models.ForeignKey(Reacao, on_delete=models.CASCADE, related_name= 'reacoes_post')
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name = 'reacoes_post')
    data = models.DateField()
