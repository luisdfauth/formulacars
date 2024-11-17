from django.forms import ModelForm
from .models import Post, Obs


class ReceitaForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'tempo_de_preparo',
            'ingredientes',
            'text',
            'foto',
        ]
        labels = {
            'name': 'Título',
            'tempo_de_preparo': 'Tempo de Preparo',
            'ingredientes': 'Ingredientes',
            'text': 'Como fazer',
            'foto': 'URL da Foto',
        }

class ObsForm(ModelForm):
    class Meta:
        model = Obs
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }