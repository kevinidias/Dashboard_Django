from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('retorna-total-vendido', views.retorna_total_vendido, name='retorna_total_vendido')
]