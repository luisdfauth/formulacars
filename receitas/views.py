from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .temp_data import movie_data
from .models import Receita
from django.shortcuts import render, get_object_or_404


def list_receitas(request):
    context = {"receita_list": movie_data}
    return render(request, 'receitas/index.html', context)

def detail_receita(request, receita_id):
    context = {'receita': movie_data[receita_id - 1]}
    return render(request, 'receitas/detail.html', context)

def search_receita(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        receita_list = Receita.objects.filter(name__icontains=search_term)
        context = {"receita_list": receita_list}
    return render(request, 'receitas/search.html', context)

def create_receita(request):
    if request.method == 'POST':
        receita_name = request.POST['name']
        receita_tempo_de_preparo = request.POST['tempo_de_preparo']
        receita_foto = request.POST['foto']
        receita = Receita(name=receita_name,
                      release_year=receita_tempo_de_preparo,
                      poster_url=receita_foto)
        receita.save()
        return HttpResponseRedirect(
            reverse('receitas:detail', args=(receita.id, )))
    else:
        return render(request, 'receitas/create.html', {})
    
def list_receitas(request):
    receita_list = Receita.objects.all()
    context = {'receita_list': receita_list}
    return render(request, 'receitas/index.html', context)

def detail_receita(request, receita_id):
    receita = Receita.objects.get(pk=receita_id)
    context = {'receita': receita}
    return render(request, 'receitas/detail.html', context)

def detail_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    context = {'receita': receita}
    return render(request, 'receitas/detail.html', context)

def update_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    if request.method == "POST":
        receita.name = request.POST['name']
        receita.tempo_de_preparo = request.POST['tempo_de_preparo']
        receita.foto = request.POST['foto']
        receita.save()
        return HttpResponseRedirect(
            reverse('receitas:detail', args=(receita.id, )))

    context = {'receita': receita}
    return render(request, 'receitas/update.html', context)


def delete_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    if request.method == "POST":
        receita.delete()
        return HttpResponseRedirect(reverse('receitas:index'))

    context = {'receita': receita}
    return render(request, 'receitas/delete.html', context)