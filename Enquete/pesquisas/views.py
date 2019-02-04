from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from .models import Questao

# Create your views here.

def index(request):
    lista_questoes_recentes = Questao.objects.order_by('-data_publicacao')[:5]
    contexto = {'lista_questoes_recentes': lista_questoes_recentes,}
    return render(request, 'pesquisas/index.html',contexto)

def detalhe(request, id_questao):
    try:
        questao = Questao.objects.get(id=id_questao)
    except Questao.DoesNotExist:
        raise Http404("Questão não existe")
    return render(request, 'pesquisas/detalhe.html', {'questao': questao})

def resultado(request, id_questao):
    resposta = 'Resultado da questão %s.'
    return HttpResponse(resposta % id_questao)

def voto(request, id_questao):
    return HttpResponse('Você está votando na questão %s.' %id_questao)