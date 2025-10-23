from django.db import models




class Cliente(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    numero = models.IntegerField()
    cep =models.CharField(max_length = 20)
    logradouro = models.CharField(max_length=30)
    estado = models.CharField(max_length=15)
    cidade = models.CharField(max_length=25)
    ativo = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.nome} cpf: {self.cpf}'



class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.TimeField(auto_now=True, null = True)
    valor_total = models.DecimalField(decimal_places=3, max_digits = 9, default=0, null = True)
    
    

class Categoria(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.nome}'
    

class Produto(models.Model):
    nome = models.CharField(max_length=25)
    Categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    unidade_de_venda = models.CharField(max_length=8)
    preco_unitario = models.DecimalField(decimal_places=3, max_digits = 9)
    quantidade_disponivel = models.DecimalField(decimal_places=3, max_digits = 9)
    data_ultima_atualizacao = models.TimeField(auto_now=True, null = True)
    data_validade = models.DateField(null=True)
   
    

    def __str__(self):
        return f'{self.nome}'


class Item_Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete= models.CASCADE)
    quantidade = models.IntegerField()






