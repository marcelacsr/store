# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse

from .models import Categoria

def index(request):
    # return HttpResponse("Olá Mundo! Você está vendo o conteúdo da view index da aplicação 'vendas'")
    frase = "Olá mundo";
    return render(request, 'vendas/index.html', {'frase': frase})

def categorias(request):
    categorias = '<br/> '.join(["%s: %s (%s)" % (cat.id, cat.nome, cat.slug) for cat in Categoria.objects.all().order_by('id')])
    return HttpResponse(categorias)

def cadastro_categoria(request):

    categorias = ', '.join(["%s: %s (%s)" % (cat.id, cat.nome, cat.slug) for cat in Categoria.objects.all().order_by('id')])

    if (request.method == 'POST'):
        cat = Categoria(nome=request.POST['nome'], slug=request.POST['slug'])
        cat.save()
        return HttpResponseRedirect(reverse('vendas:cadastro_categoria'), {'categorias': categorias})

    return render(request, 'vendas/cadastro_categoria.html', {'categorias': categorias})