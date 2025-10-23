from django.shortcuts import render, redirect, get_object_or_404
from Site.models import *
from Site.forms import *
from django.forms.models import inlineformset_factory
from django.db.models import F #
from django.contrib.auth.decorators import login_required
# Create your views here.




@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def detalhar_cliente(request, id_cliente):

    cl = get_object_or_404(Cliente, pk = id_cliente)

    return render(request, "detalhar_cliente.html", context = {"cliente": cl})




@login_required
def categorias(request):
    contexto = {'Categorias':Categoria.objects.all()}

    return render(request, 'categorias.html', context = contexto)

@login_required
def produtos_por_categoria(request, id_categoria):
    #do jeito burro

    #ver se existe
    a = get_object_or_404(Categoria, pk = id_categoria)

    produtos_da_categoria = []
    for produtos in Produto.objects.all():
        if (produtos.Categoria.id == a.id):
            produtos_da_categoria.append(produtos)
    
    return render(request, 'produtos_por_categoria.html', context = {"Produtos":produtos_da_categoria, "categoria":id_categoria})

@login_required
def cadastrar_produto_por_categoria(request, id_cat):
    #ver se existe
    a = get_object_or_404(Categoria, pk = id_cat)
    

    if (request.method == "POST"):
        produtoF = ProdutoFM(request.POST)

        if (produtoF.is_valid()):
            produtoF.save()
            return redirect("produtosPorCategoria", id_categoria = id_cat)
        else:
            return render(request, 'cadastrarProdutosPorCategoria.html', context={"form":produtoF})  
    
    else:
        produtoF = ProdutoFM()
        return render(request, 'cadastrarProdutosPorCategoria.html', context={"form":produtoF})    

        
@login_required
def exluir_produto(request, id_produto):

    a = get_object_or_404(Produto, pk = id_produto)
    categoria_id = a.Categoria.id

    

    a.delete()

    return redirect("produtosPorCategoria", id_categoria = categoria_id)


@login_required
def editar_produto(request, id_produto):
    # 1. Recupera o objeto antigo (instância)
    antigo_produto = get_object_or_404(Produto, pk=id_produto)
    
    # Guarda o ID da Categoria antes de qualquer alteração, para o redirecionamento
    id_categoria = antigo_produto.Categoria.id 

    if request.method == "POST":
        
        # 2. Cria o formulário, passando os DADOS DO POST E a INSTÂNCIA
        # Isso diz ao Django para ATUALIZAR 'antigo_produto' com 'request.POST'
        form = ProdutoFM(request.POST, instance=antigo_produto)
        
        if form.is_valid():
            # 3. Salva a instância, atualizando-a no banco de dados.
            form.save() 
            
            # 4. Redireciona para a lista de produtos da categoria original
            # O ID da Categoria é o que você precisa passar, não a instância do Produto.
            return redirect("produtosPorCategoria", id_categoria=id_categoria)

    else:
        # 5. Visão GET (Exibir formulário de edição)
        # Cria o formulário, passando a INSTÂNCIA. Isso PREENCHE os campos do form.
        form = ProdutoFM(instance=antigo_produto)

        # 6. Renderiza o template com o formulário preenchido
        return render(request, 'cadastrarProdutosPorCategoria.html', context={"form": form})
    
@login_required
def ver_produto(request, id_produto):

    a = get_object_or_404(Produto, pk = id_produto)


    return render(request, "ver_produto.html", context = {"produto":a})



@login_required
def cadastrar_categoria(request):
   
   if (request.method == "POST"):
       form = CategoriaFM(request.POST)
       
       if (form.is_valid()):
           form.save()
           return redirect('categorias')
   else:
       form = CategoriaFM()
       return render(request, 'cadastrarCategoria.html', context = {'form':form})
   

@login_required
def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk = id)

    categoria.delete()

    return redirect('categorias')

@login_required
def editar_categoria(request, id):
    if (request.method == "POST"):
        novo = CategoriaFM(request.POST)
        antigo = get_object_or_404(Categoria, pk=id)

        if novo.is_valid():
            antigo.delete()
            novo.save()
            return redirect('categorias')
    else:
        a = get_object_or_404(Categoria, pk = id)


        return render(request, "cadastrarCategoria.html", context = {"form":CategoriaFM(instance = a)})
    

@login_required
def clientes(request):
    clientes = Cliente.objects.all()

    return render(request, "clientes.html", context = {"clientes":clientes})


@login_required
def criar_cliente(request):

    if (request.method == "POST"):
        c = ClienteFM(request.POST)

        if c.is_valid():
            c.save()
            return redirect('clientes')
    else:
        c = ClienteFM()
        return render(request, 'criar_cliente.html', context = {"form":c})

@login_required
def excluir_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk = id_cliente)

    cliente.delete()

    return redirect('clientes')

@login_required
def editar_cliente(request, id_cliente):
    antigo = get_object_or_404(Cliente, pk = id_cliente)

    if (request.method =="POST"):
        novo = ClienteFM(request.POST)
        

        if novo.is_valid():
            antigo.delete()
            novo.save()
            return redirect('clientes')
    else:
        return render(request, 'criar_cliente.html', context = {"form":ClienteFM(instance = antigo)})
    
@login_required
def pedidos(request):
    pedidos = Pedido.objects.all()
    
    return render(request, 'pedidos.html', context = {"pedidos":pedidos})

@login_required
def detalhar_pedido(request, id_pedido):
    items_pedidos_lista = []
    for items in Item_Pedido.objects.all():
        if (items.pedido.id == id_pedido):
            items_pedidos_lista.append(items)

    pedido = get_object_or_404(Pedido, pk = id_pedido)
    
    return render(request, 'detalharPedidos.html', context = {"pedido":pedido, "lista_de_items_pedidos":items_pedidos_lista})


@login_required
def criar_pedido(request):
    if (request.method == "POST"):
        a = PedidoFM(request.POST)

        if (a.is_valid()):
            a.save()

            return redirect('adicionar_produto', id_ped = a.instance.pk)
        else:
            return render(request, "criar_pedido.html", context = {"form":PedidoFM()})

            
    else:
         return render(request, "criar_pedido.html", context = {"form":PedidoFM()})
    

@login_required
def adicionar_produto(request, id_ped):

    # 1. Recupera a instância do Pedido
    pedido_instance = get_object_or_404(Pedido, pk=id_ped) 

    if request.method == "POST":
        a = Item_PedidoFM(request.POST)

        if a.is_valid():
            novo_item = a.save(commit=False)
            
            # 2. Atribui a instância do Pedido
            novo_item.pedido = pedido_instance 

            # Garante que o preco_unitario do Produto seja carregado
            # (Se o Produto for um FK, o Django geralmente carrega, mas é bom garantir)
            # Você precisa carregar o Produto para obter o preço (ou usar o ID)
            preco = novo_item.produto.preco_unitario * novo_item.quantidade

            novo_item.save()

            # 3. ATUALIZAÇÃO ATÔMICA DO VALOR_TOTAL DO PEDIDO
            # Isso garante que o valor seja salvo corretamente no banco, 
            # mesmo que vários usuários acessem simultaneamente.
            Pedido.objects.filter(pk=id_ped).update(
                valor_total=F('valor_total') + preco
            )
            
            # 4. Redirecionamento Correto: volta para o loop do mesmo pedido
            return redirect('adicionar_produto', id_ped=id_ped) 
    
    else:
        a = Item_PedidoFM()

        return render(request, 'adicionar_produto.html', context = {"form": a, "pedido": pedido_instance})

@login_required
def excluir_pedido(request, id_pedido):
    a = get_object_or_404(Pedido, pk = id_pedido)

    a.delete()

    return redirect('pedidos')

