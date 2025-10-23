# Gerenciador de frutaria

🍇 FRUTARIA RIO - Sistema de Gerenciamento de E-commerce

<p align="center"> <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellowgreen" alt="Status do Projeto"> <img src="https://img.shields.io/badge/Feito%20com-Django-092E20?logo=django" alt="Tecnologia Principal"> <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20Puro-blue" alt="Frontend"> </p>

📋 Sobre o Projeto

O FRUTARIA RIO é um sistema web de gestão de pedidos e clientes desenvolvido com o framework Django. O projeto foca em fornecer uma interface administrativa (não é a loja virtual em si) para que a frutaria possa cadastrar seu catálogo de produtos, gerenciar informações de clientes, criar pedidos e monitorar o valor total das transações.

O design do sistema utiliza CSS puro com uma paleta de cores inspirada em frutas (Verde, Laranja e Amarelo), garantindo uma experiência visual coesa e agradável.

✨ Funcionalidades

O sistema oferece as seguintes módulos de gestão:

🍓 Gestão de Catálogo (Produtos e Categorias)

    Categorias: Cadastro, listagem, edição e exclusão de categorias de frutas, legumes, etc.

    Produtos: Detalhamento do estoque (quantidade, unidade de venda: Kg/Un), preço unitário, e informações de validade.

👥 Gestão de Clientes

    Cadastro e listagem de clientes com informações detalhadas (Nome, CPF, Endereço completo).

    Visualização do status do cliente (ATIVO / NAO).

🛒 Gestão de Pedidos

    Criação de novos pedidos, vinculando-os a um cliente existente.

    Adição Dinâmica de Itens: Adicionar múltiplos produtos e suas quantidades a um pedido.

    Cálculo Automático de Total: O sistema calcula e atualiza o valor_total do pedido de forma atômica (usando F() expressions do Django) a cada item adicionado.

    Listagem e detalhamento de todos os pedidos.

🛠️ Tecnologias Utilizadas

    Backend: Python 3.9+

    Framework: Django (4.2.x)

    Banco de Dados: SQLite (padrão de desenvolvimento)

    Frontend: HTML5 e CSS3 (Design customizado com foco em usabilidade).

🚀 Como Rodar o Projeto

Siga os passos abaixo para clonar e executar o projeto em sua máquina local.

Pré-requisitos

1. tenha uma versão do python3
2. recomenda-se a instalação de um ambiente virtual atravez do venv
3. instale o django
4. e rode e seja feliz
5. 

Você precisa ter o Python 3.9 ou superior instalado.
