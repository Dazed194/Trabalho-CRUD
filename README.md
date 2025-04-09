# Trabalho-CRUD



# Explicação do Funcionamento

# O sistema foi desenvolvido em Python usando SQLite para armazenamento local. O código está organizado em funções específicas:

    Funções de Banco de Dados:

        criar_conexao(): Conecta ao arquivo estoque.db

        criar_tabela(): Cria a tabela produtos se não existir

    Operações CRUD:

        criar_produto(): Adiciona novos itens ao estoque

        listar_produtos(): Mostra todos os produtos formatados em tabela

        atualizar_produto(): Modifica quantidade e/ou preço

        deletar_produto(): Remove produtos por ID

    Interface do Usuário:

        menu(): Mostra as opções e valida entrada

        main(): Controla o fluxo principal


# Tratamento de Erros

    Nomes duplicados (campo UNIQUE)

    IDs inexistentes

    Valores negativos para quantidade/preço

    Tipos de dados inválidos

    Confirmação antes de deletar


# Problemas e Soluções
Dados não persistiam	Adicionamos conn.commit()

Listagem desorganizada	Implementamos formatação com str.format()

Atualização parcial	Usamos verificações is not None

Listagem desorganizada	Implementamos formatação com str.format()

# Exemplos de Testes Realizados
# Teste 1 - Cadastro Válido

Adicionar novo produto

Nome: Caneta

Quantidade: 50

Preço: 1.20

→ "Produto adicionado com sucesso!"

# Teste 2 - Tentativa de Nome Repetido


Adicionar novo produto
Nome: Caneta

→ "Erro: Já existe um produto com este nome."

# Teste 3 - Atualização Parcial


Atualizar produto
ID: 1

Nova quantidade: 45

Novo preço: (vazio)

→ "Produto atualizado com sucesso!"

# Teste 4 - Remoção com Confirmação


Remover produto
ID: 1

Tem certeza? (s/n): s

→ "Produto removido com sucesso!"

# Teste 5 - Tratamento de Erros


Adicionar novo produto
Nome: Lapis

Quantidade: -10

→ "Erro: Quantidade deve ser positiva."

# Como Executar

    Salve o código como estoque.py

    Execute no terminal:
    
    python estoque.py

    Use o menu interativo para testar todas as funcionalidades


# Alunos: [Murilo Silva Vilarouca, Joao Victor carvalho]



Atualização parcial	Usamos verificações is not None
