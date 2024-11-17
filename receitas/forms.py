from django.forms import ModelForm
from .models import Receita


class ReceitaForm(ModelForm):
    class Meta:
        model = Receita
        fields = [
            'name',
            'tempo_de_preparo',
            'foto',
        ]
        labels = {
            'name': 'Título',
            'tempo_de_preparo': 'Tempo de Preparo',
            'foto': 'URL da Foto',
        }