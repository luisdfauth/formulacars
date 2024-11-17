from django.db import models
from django.conf import settings


class Receita(models.Model):
    name = models.CharField(max_length=255)
    tempo_de_preparo = models.CharField(max_length=15)
    foto = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name} ({self.tempo_de_preparo})'


class Obs(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, related_name='receitas_obs')
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
    