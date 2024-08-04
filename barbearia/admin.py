from django.contrib import admin
from .models import Endereco, Barbearia, Barbeiro, Servico, Cliente, Agendamento

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'bairro', 'cidade', 'estado', 'cep')
    search_fields = ('logradouro', 'bairro', 'cidade', 'estado', 'cep')


@admin.register(Barbearia)
class BarbeariaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'horario_funcionamento', 'endereco')
    search_fields = ('nome', 'cnpj')
    list_filter = ('horario_funcionamento',)


@admin.register(Barbeiro)
class BarbeiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'disponibilidade', 'barbearia')
    search_fields = ('nome', 'cpf')
    list_filter = ('barbearia',)


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'duracao', 'categoria')
    search_fields = ('nome', 'categoria')
    list_filter = ('categoria',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'cpf')
    search_fields = ('nome', 'email', 'cpf')


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'barbeiro', 'servico', 'data_hora', 'status', 'barbearia')
    search_fields = ('cliente__nome', 'barbeiro__nome', 'servico__nome', 'status')
    list_filter = ('status', 'barbearia', 'data_hora')
    date_hierarchy = 'data_hora'
