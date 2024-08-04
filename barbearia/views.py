from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Endereco, Barbearia, Barbeiro, Servico, Cliente, Agendamento
from .serializers import EnderecoSerializer, BarbeariaSerializer, BarbeiroSerializer, ServicoSerializer, ClienteSerializer, AgendamentoSerializer

class EnderecoListCreate(APIView):
    def get(self, request):
        enderecos = Endereco.objects.all()
        serializer = EnderecoSerializer(enderecos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EnderecoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnderecoDetail(APIView):
    def get_object(self, pk):
        try:
            return Endereco.objects.get(pk=pk)
        except Endereco.DoesNotExist:
            return None

    def get(self, request, pk):
        endereco = self.get_object(pk)
        if endereco is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EnderecoSerializer(endereco)
        return Response(serializer.data)

    def put(self, request, pk):
        endereco = self.get_object(pk)
        if endereco is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EnderecoSerializer(endereco, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        endereco = self.get_object(pk)
        if endereco is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        endereco.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BarbeariaListCreate(APIView):
    def get(self, request):
        barbearias = Barbearia.objects.all()
        serializer = BarbeariaSerializer(barbearias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BarbeariaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BarbeariaDetail(APIView):
    def get_object(self, pk):
        try:
            return Barbearia.objects.get(pk=pk)
        except Barbearia.DoesNotExist:
            return None

    def get(self, request, pk):
        barbearia = self.get_object(pk)
        if barbearia is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BarbeariaSerializer(barbearia)
        return Response(serializer.data)

    def put(self, request, pk):
        barbearia = self.get_object(pk)
        if barbearia is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BarbeariaSerializer(barbearia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        barbearia = self.get_object(pk)
        if barbearia is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        barbearia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BarbeiroListCreate(APIView):
    def get(self, request):
        barbeiros = Barbeiro.objects.all()
        serializer = BarbeiroSerializer(barbeiros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BarbeiroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BarbeiroDetail(APIView):
    def get_object(self, pk):
        try:
            return Barbeiro.objects.get(pk=pk)
        except Barbeiro.DoesNotExist:
            return None

    def get(self, request, pk):
        barbeiro = self.get_object(pk)
        if barbeiro is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BarbeiroSerializer(barbeiro)
        return Response(serializer.data)

    def put(self, request, pk):
        barbeiro = self.get_object(pk)
        if barbeiro is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BarbeiroSerializer(barbeiro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        barbeiro = self.get_object(pk)
        if barbeiro is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        barbeiro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ServicoListCreate(APIView):
    def get(self, request):
        servicos = Servico.objects.all()
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServicoDetail(APIView):
    def get_object(self, pk):
        try:
            return Servico.objects.get(pk=pk)
        except Servico.DoesNotExist:
            return None

    def get(self, request, pk):
        servico = self.get_object(pk)
        if servico is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ServicoSerializer(servico)
        return Response(serializer.data)

    def put(self, request, pk):
        servico = self.get_object(pk)
        if servico is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ServicoSerializer(servico, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        servico = self.get_object(pk)
        if servico is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        servico.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClienteListCreate(APIView):
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteDetail(APIView):
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return None

    def get(self, request, pk):
        cliente = self.get_object(pk)
        if cliente is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    def put(self, request, pk):
        cliente = self.get_object(pk)
        if cliente is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cliente = self.get_object(pk)
        if cliente is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AgendamentoListCreate(APIView):
    def get(self, request):
        agendamentos = Agendamento.objects.all()
        serializer = AgendamentoSerializer(agendamentos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AgendamentoDetail(APIView):
    def get_object(self, pk):
        try:
            return Agendamento.objects.get(pk=pk)
        except Agendamento.DoesNotExist:
            return None

    def get(self, request, pk):
        agendamento = self.get_object(pk)
        if agendamento is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AgendamentoSerializer(agendamento)
        return Response(serializer.data)

    def put(self, request, pk):
        agendamento = self.get_object(pk)
        if agendamento is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AgendamentoSerializer(agendamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        agendamento = self.get_object(pk)
        if agendamento is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        agendamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)