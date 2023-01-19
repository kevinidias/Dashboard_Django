from django.shortcuts import render
from django.http import HttpResponse
from .models import Vendas
from django.http import JsonResponse
from django.db.models import Sum

def home(request):
    return render(request, 'home.html')

def retorna_total_vendido(request):
    total_vendas = Vendas.objects.all().aggregate(Sum('total'))['total__sum']
    return JsonResponse({'total': total_vendas})