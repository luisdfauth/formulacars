from django.urls import path
from .views import (
    ReceitaListView, ReceitaDetailView, ReceitaCreateView, 
    ReceitaUpdateView, ReceitaDeleteView, ObsCreateView, ReceitaSearchView
)
from . import views

app_name = 'receitas'
urlpatterns = [
    path('', ReceitaListView.as_view(), name='index'),
    path('search/', ReceitaSearchView.as_view(), name='search'),
    path('create/', ReceitaCreateView.as_view(), name='create'),
    path('<int:pk>/', ReceitaDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', ReceitaUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ReceitaDeleteView.as_view(), name='delete'),
    path('<int:receita_id>/obs/', ObsCreateView.as_view(), name='add_obs'),
    path('lists/', views.ListListView.as_view(), name='lists'),
    path('lists/create', views.ListCreateView.as_view(), name='create-list'),
]