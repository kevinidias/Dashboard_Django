from django.contrib import admin
from .models import Vendas, Vendedor, Produto, Despesas

admin.site.register(Vendas)
admin.site.register(Vendedor)
admin.site.register(Produto)
admin.site.register(Despesas)
