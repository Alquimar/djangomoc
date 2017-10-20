from django.contrib import admin
from cliente.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    date_hierarchy = 'data_nascimento'
    list_display = ('nome', 'data_nascimento', 'salario', 'email', 'filhos')
    list_filter = ('data_nascimento', 'salario', 'filhos')
    search_fields = ('nome', 'data_nascimento', 'email')

admin.site.register(Cliente, ClienteAdmin)
