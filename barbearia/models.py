from django.db import models

class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.logradouro}, {self.numero} - {self.bairro}, {self.cidade} - {self.estado}, {self.cep}'


class Barbearia(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    horario_funcionamento = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Barbeiro(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    disponibilidade = models.CharField(max_length=255)
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE, related_name='barbeiros')

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    duracao = models.DurationField()
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='agendamentos_cliente')
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE, related_name='agendamentos_barbeiro')
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='agendamentos_servico')
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=50)
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE, related_name='agendamentos')

    def __str__(self):
        return f'{self.cliente} - {self.servico} em {self.data_hora}'
