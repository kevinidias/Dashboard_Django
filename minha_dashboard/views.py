from django.shortcuts import render
from django.http import HttpResponse
from .models import Vendas
from django.http import JsonResponse
from django.db.models import Sum
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def retorna_total_vendido(request):
    total_vendas = Vendas.objects.all().aggregate(Sum('total'))['total__sum']
    return JsonResponse({'total': total_vendas})

def relatorio_faturamento(request):
    x = Vendas.objects.all()

    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    cont = 0
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12):
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        
        y = sum([i.total for i in x if i.data.month == mes and i.data.year == ano])
        labels.append(meses[mes-1])
        data.append(y)
        cont += 1

    data_json = {'data': data[::-1], 'labels': labels[::-1]}

    return JsonResponse(data_json)