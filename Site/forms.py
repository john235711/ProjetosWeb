# forms.py

from django import forms
from .models import * # Importa todos os models definidos

# --- Widgets Customizados Reutilizáveis ---

# Widget para campos de data com o calendário nativo (HTML5 type="date")
class DateInput(forms.DateInput):
    input_type = 'date'
    # Define o formato de exibição da data para o backend
    format = '%Y-%m-%d'

# Widget para campos de hora (HTML5 type="time")
class TimeInput(forms.TimeInput):
    input_type = 'time'

# Widget base para a maioria dos campos de texto e número
TEXT_INPUT_WIDGET = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite aqui...'})
NUMBER_INPUT_WIDGET = forms.NumberInput(attrs={'class': 'form-control'})
SELECT_WIDGET = forms.Select(attrs={'class': 'form-control'})
EMAIL_INPUT_WIDGET = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seuemail@exemplo.com'})


# --- ModelForms com Widgets ---

class CategoriaFM(forms.ModelForm):
    class Meta():
        model = Categoria
        fields = ["nome"]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Eletrônicos'}),
        }


class ProdutoFM(forms.ModelForm):
    class Meta():
        model = Produto
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Produto'}),
            # Usando o widget SELECT padrão, mas adicionando a classe
            'Categoria': SELECT_WIDGET, 
            'unidade_de_venda': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Kg, Un, Lt'}),
            'preco_unitario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 10.99', 'step': '0.01'}),
            'quantidade_disponivel': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 50.00', 'step': '0.01'}),
            
            # Usando o TimeInput customizado para o campo TimeField
            'data_ultima_atualizacao': TimeInput(attrs={'class': 'form-control'}),
            
            # Usando o DateInput customizado para o campo DateField
            'data_validade': DateInput(attrs={'class': 'form-control'}),
        }

class ClienteFM(forms.ModelForm):
    class Meta():
        model = Cliente
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primeiro Nome'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
            'email': EMAIL_INPUT_WIDGET,
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00', 'maxlength': '11'}),
            'numero': NUMBER_INPUT_WIDGET,
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00000-000'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua, Avenida, etc.'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: BA'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Salvador'}),
            # Checkbox estilizado (ou RadioSelect, dependendo da sua preferência)
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
        }
        

class PedidoFM(forms.ModelForm):
    class Meta():
        model = Pedido
        fields = ["cliente"]
        # Apenas o campo cliente é exibido, e usamos o SELECT_WIDGET
        widgets = {
            'cliente': SELECT_WIDGET,
            
            # Os campos 'data_pedido' e 'valor_total' são excluídos (ou definidos pelo model) 
            # mas se fossem exibidos, exigiriam TimeInput e NumberInput respectivamente.
        }

class Item_PedidoFM(forms.ModelForm):
    class Meta():
        model = Item_Pedido
        exclude = ["pedido"]
        widgets = {
            # Ambos os campos usam o widget SELECT padrão, mas com classes
            'produto': SELECT_WIDGET, 
            'quantidade': NUMBER_INPUT_WIDGET,
        }