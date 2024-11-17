from django.urls import path

from . import views

app_name = 'receitas'
urlpatterns = [
    path('', views.list_receitas, name='index'),
    path('search/', views.search_receita, name='search'),
    path('create/', views.create_receita, name='create'),
    path('<int:receita_id>/', views.detail_receita, name='detail'),
    path('update/<int:receita_id>/', views.update_receita, name='update'),
    path('delete/<int:receita_id>/', views.delete_receita, name='delete'),
]