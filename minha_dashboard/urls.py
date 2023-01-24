from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('retorna-total-vendido', views.retorna_total_vendido, name='retorna_total_vendido'),
    path('relatorio_faturamento', views.relatorio_faturamento, name='relatorio_returamento'),
    path('relatorio_produtos', views.relatorio_produtos, name='relatorio_produtos')
]