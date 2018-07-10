from django.urls import path
from . import views

app_name = 'vendas'

urlpatterns = [
    path('', views.index, name='index'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/cadastro', views.cadastro_categoria, name='cadastro_categoria'),
]
