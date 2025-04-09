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
#Listagem desorganizada	Implementamos formatação com str.format()
#Atualização parcial	Usamos verificações is not None
