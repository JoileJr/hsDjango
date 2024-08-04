from rest_framework import serializers
from .models import Endereco, Barbearia, Barbeiro, Servico, Cliente, Agendamento

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class BarbeariaSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()

    class Meta:
        model = Barbearia
        fields = '__all__'

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        endereco, created = Endereco.objects.update_or_create(
            id=endereco_data.get('id'), defaults=endereco_data
        )
        barbearia = Barbearia.objects.create(endereco=endereco, **validated_data)
        return barbearia

    def update(self, instance, validated_data):
        endereco_data = validated_data.pop('endereco', None)

        if endereco_data:
            endereco_id = endereco_data.get('id')
            if endereco_id:
                endereco, _ = Endereco.objects.update_or_create(
                    id=endereco_id, defaults=endereco_data
                )
            else:
                endereco = Endereco.objects.create(**endereco_data)
            instance.endereco = endereco

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

class BarbeiroSerializer(serializers.ModelSerializer):
    barbearia = BarbeariaSerializer()

    class Meta:
        model = Barbeiro
        fields = '__all__'

    def create(self, validated_data):
        barbearia_data = validated_data.pop('barbearia')
        barbearia_id = barbearia_data.get('id')

        if barbearia_id:
            try:
                barbearia = Barbearia.objects.get(id=barbearia_id)
            except Barbearia.DoesNotExist:
                raise serializers.ValidationError("Barbearia com o ID fornecido não existe.")
        
        barbeiro = Barbeiro.objects.create(barbearia=barbearia, **validated_data)
        return barbeiro
    
    def update(self, instance, validated_data):
        barbearia_data = validated_data.pop('barbearia')
        barbearia_id = barbearia_data.get('id')

        if barbearia_id:
            try:
                barbearia = Barbearia.objects.get(id=barbearia_id)
                if barbearia is not None:
                    instance.barbearia = barbearia
            except Barbearia.DoesNotExist:
                raise serializers.ValidationError("Barbearia com o ID fornecido não existe.")
        
         # Atualiza os outros atributos da instância
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Salva a instância atualizada
        instance.save()
        return instance
    
        
class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class AgendamentoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    barbeiro = BarbeiroSerializer()
    servico = ServicoSerializer()
    barbearia = BarbeariaSerializer()

    class Meta:
        model = Agendamento
        fields = '__all__'

    def create(self, validated_data):
        cliente_data = validated_data.pop('cliente')
        barbeiro_data = validated_data.pop('barbeiro')
        servico_data = validated_data.pop('servico')
        barbearia_data = validated_data.pop('barbearia')

        cliente = Cliente.objects.create(**cliente_data)
        barbeiro = Barbeiro.objects.create(**barbeiro_data)
        servico = Servico.objects.create(**servico_data)
        barbearia = Barbearia.objects.create(**barbearia_data)

        agendamento = Agendamento.objects.create(
            cliente=cliente,
            barbeiro=barbeiro,
            servico=servico,
            barbearia=barbearia,
            **validated_data
        )
        return agendamento

    def update(self, instance, validated_data):
        cliente_data = validated_data.pop('cliente', None)
        barbeiro_data = validated_data.pop('barbeiro', None)
        servico_data = validated_data.pop('servico', None)
        barbearia_data = validated_data.pop('barbearia', None)

        if cliente_data:
            cliente, created = Cliente.objects.get_or_create(**cliente_data)
            instance.cliente = cliente
        if barbeiro_data:
            barbeiro, created = Barbeiro.objects.get_or_create(**barbeiro_data)
            instance.barbeiro = barbeiro
        if servico_data:
            servico, created = Servico.objects.get_or_create(**servico_data)
            instance.servico = servico
        if barbearia_data:
            barbearia, created = Barbearia.objects.get_or_create(**barbearia_data)
            instance.barbearia = barbearia

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
