from django.urls import path
from .views import (EnderecoListCreate, EnderecoDetail,
                    BarbeariaListCreate, BarbeariaDetail,
                    BarbeiroListCreate, BarbeiroDetail,
                    ServicoListCreate, ServicoDetail,
                    ClienteListCreate, ClienteDetail,
                    AgendamentoListCreate, AgendamentoDetail)

urlpatterns = [
    path('enderecos/', EnderecoListCreate.as_view(), name='endereco-list-create'),
    path('enderecos/<int:pk>/', EnderecoDetail.as_view(), name='endereco-detail'),

    path('barbearias/', BarbeariaListCreate.as_view(), name='barbearia-list-create'),
    path('barbearias/<int:pk>/', BarbeariaDetail.as_view(), name='barbearia-detail'),

    path('barbeiros/', BarbeiroListCreate.as_view(), name='barbeiro-list-create'),
    path('barbeiros/<int:pk>/', BarbeiroDetail.as_view(), name='barbeiro-detail'),

    path('servicos/', ServicoListCreate.as_view(), name='servico-list-create'),
    path('servicos/<int:pk>/', ServicoDetail.as_view(), name='servico-detail'),

    path('clientes/', ClienteListCreate.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),

    path('agendamentos/', AgendamentoListCreate.as_view(), name='agendamento-list-create'),
    path('agendamentos/<int:pk>/', AgendamentoDetail.as_view(), name='agendamento-detail'),
]
