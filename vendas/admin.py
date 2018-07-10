from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categoria, Produto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    search_fields = ['nome', 'slug']

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'categoria', 'preco', 'estoque', 'disponivel', 'data_cadastramento', 'data_atualizacao']
    search_fields = ('nome', 'categoria', 'disponivel', 'data_cadastramento')

admin.site.register(Categoria, CategoriaAdmin)  # Registre a classe Categoria com os produtos
                                                # definidos em CategoriaAdmin
admin.site.register(Produto, ProdutoAdmin)
list_filter = ('data_cadastramento',)
list_filter = ('categoria',)
date_hierarchy = 'data_cadastramento'
ordering = ('-data_cadastramento',)
fields = ('categoria', 'nome', 'slug', 'descricao', 'preco', 'estoque')