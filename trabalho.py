import sqlite3
from sqlite3 import Error

def criar_conexao(db_file):
    """Cria uma conexão com o banco de dados SQLite"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Conexão com SQLite estabelecida (versão {sqlite3.version})")
        return conn
    except Error as e:
        print(e)
    
    return conn

def criar_tabela(conn):
    """Cria a tabela produtos se não existir"""
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        );
        """)
        print("Tabela 'produtos' criada ou já existente.")
    except Error as e:
        print(f"Erro ao criar tabela: {e}")

def criar_produto(conn, produto):
    """Insere um novo produto no estoque"""
    sql = ''' INSERT INTO produtos(nome, quantidade, preco)
              VALUES(?,?,?) '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, produto)
        conn.commit()
        print("Produto adicionado com sucesso!")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print("Erro: Já existe um produto com este nome.")
    except Error as e:
        print(f"Erro ao inserir produto: {e}")
    return None

def listar_produtos(conn):
    """Lista todos os produtos do estoque"""
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        
        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
            return
        
        print("\nLista de Produtos:")
        print("-" * 50)
        print("{:<5} {:<20} {:<10} {:<10}".format("ID", "Nome", "Quantidade", "Preço"))
        print("-" * 50)
        for produto in produtos:
            print("{:<5} {:<20} {:<10} {:<10.2f}".format(produto[0], produto[1], produto[2], produto[3]))
        print("-" * 50)
    except Error as e:
        print(f"Erro ao listar produtos: {e}")

def atualizar_produto(conn, produto_id, nova_quantidade=None, novo_preco=None):
    """Atualiza quantidade e/ou preço de um produto"""
    cursor = conn.cursor()
    
    # Verifica se o produto existe
    cursor.execute("SELECT id FROM produtos WHERE id = ?", (produto_id,))
    if cursor.fetchone() is None:
        print("Erro: Produto com este ID não encontrado.")
        return
    
    # Atualiza os campos fornecidos
    if nova_quantidade is not None and novo_preco is not None:
        sql = ''' UPDATE produtos
                  SET quantidade = ?, preco = ?
                  WHERE id = ? '''
        cursor.execute(sql, (nova_quantidade, novo_preco, produto_id))
    elif nova_quantidade is not None:
        sql = ''' UPDATE produtos
                  SET quantidade = ?
                  WHERE id = ? '''
        cursor.execute(sql, (nova_quantidade, produto_id))
    elif novo_preco is not None:
        sql = ''' UPDATE produtos
                  SET preco = ?
                  WHERE id = ? '''
        cursor.execute(sql, (novo_preco, produto_id))
    else:
        print("Nada para atualizar.")
        return
    
    conn.commit()
    print("Produto atualizado com sucesso!")

def deletar_produto(conn, produto_id):
    """Remove um produto do estoque pelo ID"""
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
        conn.commit()
        
        if cursor.rowcount == 0:
            print("Erro: Nenhum produto encontrado com este ID.")
        else:
            print("Produto removido com sucesso!")
    except Error as e:
        print(f"Erro ao remover produto: {e}")

def menu():
    """Exibe o menu de opções"""
    print("\nSistema de Gerenciamento de Estoque")
    print("1. Adicionar novo produto")
    print("2. Listar todos os produtos")
    print("3. Atualizar produto")
    print("4. Remover produto")
    print("5. Sair")
    
    while True:
        try:
            opcao = int(input("Escolha uma opção (1-5): "))
            if 1 <= opcao <= 5:
                return opcao
            print("Opção inválida. Digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 5.")

def main():
    # Configuração do banco de dados
    database = "estoque.db"
    
    # Cria conexão e tabela
    conn = criar_conexao(database)
    if conn is not None:
        criar_tabela(conn)
    else:
        print("Erro! Não foi possível estabelecer conexão com o banco de dados.")
        return
    
    # Loop principal do programa
    while True:
        opcao = menu()
        
        if opcao == 1:  # Adicionar produto
            print("\nAdicionar Novo Produto")
            nome = input("Nome do produto: ").strip()
            
            try:
                quantidade = int(input("Quantidade: "))
                preco = float(input("Preço unitário: "))
                
                if quantidade < 0 or preco < 0:
                    print("Erro: Quantidade e preço devem ser valores positivos.")
                    continue
                
                criar_produto(conn, (nome, quantidade, preco))
            except ValueError:
                print("Erro: Quantidade deve ser um número inteiro e preço um número real.")
        
        elif opcao == 2:  # Listar produtos
            listar_produtos(conn)
        
        elif opcao == 3:  # Atualizar produto
            print("\nAtualizar Produto")
            listar_produtos(conn)
            
            try:
                produto_id = int(input("ID do produto a ser atualizado: "))
                
                print("Deixe em branco para manter o valor atual.")
                nova_quantidade = input("Nova quantidade: ")
                novo_preco = input("Novo preço: ")
                
                # Processa os inputs
                qnt = int(nova_quantidade) if nova_quantidade.strip() else None
                prc = float(novo_preco) if novo_preco.strip() else None
                
                if qnt is not None and qnt < 0:
                    print("Erro: Quantidade deve ser positiva.")
                    continue
                if prc is not None and prc < 0:
                    print("Erro: Preço deve ser positivo.")
                    continue
                
                if qnt is None and prc is None:
                    print("Nenhuma alteração solicitada.")
                else:
                    atualizar_produto(conn, produto_id, qnt, prc)
            except ValueError:
                print("Erro: ID deve ser um número inteiro. Quantidade e preço devem ser números.")
        
        elif opcao == 4:  # Remover produto
            print("\nRemover Produto")
            listar_produtos(conn)
            
            try:
                produto_id = int(input("ID do produto a ser removido: "))
                confirmacao = input(f"Tem certeza que deseja remover o produto ID {produto_id}? (s/n): ")
                
                if confirmacao.lower() == 's':
                    deletar_produto(conn, produto_id)
                else:
                    print("Operação cancelada.")
            except ValueError:
                print("Erro: ID deve ser um número inteiro.")
        
        elif opcao == 5:  # Sair
            print("Encerrando o sistema...")
            break
    
    # Fecha a conexão com o banco de dados
    conn.close()

if __name__ == '__main__':
    main()