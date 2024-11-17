from django.db import models
from django.conf import settings


class Post(models.Model):
    name = models.CharField(max_length=255)
    tempo_de_preparo = models.CharField(max_length=15)
    text = models.CharField(max_length=255)
    ingredientes = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    foto = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name} ({self.tempo_de_preparo})'


class Obs(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    receita = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
    
class List(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    receitas = models.ManyToManyField(Post)

    def __str__(self):
        return f'{self.nome} by {self.autor}'
    
