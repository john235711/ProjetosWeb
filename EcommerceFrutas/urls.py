"""
URL configuration for EcommerceFrutas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from Site import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name = "registration/login.html"), name = "login"),
    path("logout/", auth_views.LogoutView.as_view(next_page ="login"), name = "logout"),
    path('admin/', admin.site.urls),
    path('', views.categorias, name = "home"),
    path('categorias/', views.categorias, name = "categorias"),
    path('cadastrarCategoria/', views.cadastrar_categoria, name = "cadastrarCategoria"),
    path("excluirCategoria/<int:id>", views.excluir_categoria, name = "excluirCategoria"),
    path("editarCategoria/<int:id>", views.editar_categoria, name = "editarCategoria"),
    path('produtosPorCategoria/<int:id_categoria>', views.produtos_por_categoria, name = "produtosPorCategoria"),
    path('cadastrarProtudoPorCategoria/<int:id_cat>', views.cadastrar_produto_por_categoria, name = "cadastrarProtudoPorCategoria"),
    path("clientes/", views.clientes, name = "clientes"),
    path("criar_cliente/", views.criar_cliente, name = "criar_cliente"),
    path('excluir_cliente/<int:id_cliente>', views.excluir_cliente, name = "excluir_cliente"),
    path('editar_cliente/<int:id_cliente>', views.editar_cliente, name = "editar_cliente"),
    path('pedidos/', views.pedidos, name = "pedidos"),
    path('detalhar_pedido/<int:id_pedido>', views.detalhar_pedido, name = "detalhar_pedido"),
    path('criar_pedido', views.criar_pedido, name = "criar_pedido"),
    path('adicionar_pedido/<int:id_ped>', views.adicionar_produto, name = "adicionar_produto"),
    path('ver_produto/<int:id_produto>', views.ver_produto, name = "ver_produto"),
    path("excluir_produto/<int:id_produto>", views.exluir_produto, name = "excluir_produto"),
    path("editar_produto/<int:id_produto>", views.editar_produto, name = "editar_produto"),
    path("excluir_pedido/<int:id_pedido>", views.excluir_pedido, name = "excluir_pedido"),
    path("detalhar_cliente/<int:id_cliente>", views.detalhar_cliente, name = "detalhar_cliente")

]
