from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Post, Comment, Category
from .forms import ReceitaForm, ObsForm
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ReceitaSearchView(ListView):
    model = Post
    template_name = 'receitas/search.html'
    context_object_name = 'receita_list'

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        return Post.objects.filter(name__icontains=query) if query else Post.objects.none()
    
class ReceitaCreateView(CreateView):
    model = Post
    form_class = ReceitaForm
    template_name = 'receitas/create.html'

    def form_valid(self, form):
        receita = form.save()
        return HttpResponseRedirect(reverse_lazy('receitas:detail', args=(receita.id,)))
    
class ReceitaListView(ListView):
    model = Post
    template_name = 'receitas/index.html'
    context_object_name = 'receita_list'

class ReceitaDetailView(DetailView):
    model = Post
    template_name = 'receitas/detail.html'
    context_object_name = 'receita'

class ReceitaUpdateView(UpdateView):
    model = Post
    form_class = ReceitaForm
    template_name = 'receitas/update.html'

    def form_valid(self, form):
        receita = form.save()
        return HttpResponseRedirect(reverse_lazy('receitas:detail', args=(receita.id,)))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['receita'] = self.get_object()  
        return context


class ReceitaDeleteView(DeleteView):
    model = Post
    template_name = 'receitas/delete.html'
    success_url = reverse_lazy('receitas:index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['receita'] = self.get_object()  
        return context


class ObsCreateView(CreateView):
    model = Comment
    form_class = ObsForm
    template_name = 'receitas/obs.html'

    def form_valid(self, form):
        # Pega o ID da receita da URL (receita_id)
        receita_id = self.kwargs['receita_id']
        # Obtém o objeto Receita (Post) relacionado
        receita = get_object_or_404(Post, pk=receita_id)
        
        # Associa a receita à nova observação
        obs = form.save(commit=False)
        obs.receita = receita
        obs.save()

        # Redireciona para a página de detalhes da receita
        return HttpResponseRedirect(reverse_lazy('receitas:detail', kwargs={'pk': receita_id}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Passa a receita atual no contexto para o template
        receita_id = self.kwargs['receita_id']
        context['receita'] = get_object_or_404(Post, pk=receita_id)
        return context

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'receitas/lists.html'
   

class CategoryView(DetailView):
    model = Category
    template_name = 'receitas/index.html'
    context_object_name = 'category'

