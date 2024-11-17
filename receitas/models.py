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


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    receita = models.ForeignKey(Post, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-date']
    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    receitas = models.ManyToManyField(Post)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} '
    
