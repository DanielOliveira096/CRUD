import sqlite3

# Função para criar o banco e tabela
# def database():
#     start = sqlite3.connect('collab_notebooks/database/database.db')
#     cursor = start.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS pedidos (
#             codigo INTEGER PRIMARY KEY AUTOINCREMENT,
#             cliente TEXT NOT NULL,
#             prato TEXT NOT NULL,
#             quantidade INTEGER NOT NULL,
#             valor_total REAL NOT NULL
#         )
#     ''')
#     start.commit()
#     start.close()


# Função Menu
def menu():
    #database()  # garante que a tabela existe
    while True:
        print("\n===== SISTEMA CONN =====")
        print("1 - Cadastrar pedido")
        print("2 - Listar pedidos")
        print("3 - Buscar pedido")
        print("4 - Atualizar pedido")
        print("5 - Remover pedido")
        print("0 - Sair")

        options = input("Escolha uma opção: ")

        if options == "1":
            creat_pedido()
        elif options == "2":
            list_pedidos()
        elif options == "3":
            search_pedido()
        elif options == "4":
            update_pedido()
        elif options == "5":
            delete_pedido()
        elif options == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Função para cadastrar pedido
def creat_pedido():
    contador = 0
    print("\n=== CADASTRAR PEDIDO ===")

    cliente = input("Digite o nome do cliente: ").strip()
    for char in cliente:
        contador += 1
        if char.isdigit():
            print("Nome Inválido!")
            return creat_pedido()
    
        
    if not cliente:
        print("Campo Vazio...")
        return creat_pedido()
    if contador < 8:
        print("Nome muito pequeno...")
        return creat_pedido()
    elif contador > 20:
        print("Nome muito grande...")
        return creat_pedido()
    
    prato = input("Digite o prato: ").strip()
    if not prato:
        print("Informação inválido!")
        return creat_pedido()
    elif prato.isdigit():
        print("Prato inválido!")
        return creat_pedido()
    
    quantidade = input("Digite a quantidade: ").strip()
    try:
        quantidade = int(quantidade)
    except ValueError:
        print("Quantidade inválida!")
        return creat_pedido()
    #quantidade = int(quantidade)
    
    if not quantidade or quantidade <= 0:
        print("Quantidade inválida!")
        return creat_pedido()

    #Corrigindo o input do valor total para aceitar números corretamente
    
    valor_total = input("Digite o valor total: ").strip()
    try:
        valor_total = float(valor_total)
    except ValueError:
        print("Valor inválido!")
        return creat_pedido()

    #####Método de restrição########
    #if not cliente or not prato or quantidade <= 0 or valor_total <= 0:
    #    print("Dados inválidos, pedido não cadastrado!")
    #    return creat_pedido()

    conn = sqlite3.connect('collab_notebooks/database/database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pedidos (cliente, prato, quantidade, valor_total)
        VALUES (?, ?, ?, ?)
    ''', (cliente, prato, quantidade, valor_total))
    conn.commit()
    conn.close()
    print("Pedido cadastrado com sucesso!!!")


# Função para listar pedidos
def list_pedidos():
    conn = sqlite3.connect('collab_notebooks/database/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()

    for linha in pedidos:
      if linha == ():
        print("\nNenhum pedido cadastrado.")
      else:
          print(f"\n- Código: {linha[0]}  \n- Cliente: {linha[1]}  \n- Prato: {linha[2]}  \n- Quantidade: {linha[3]}  \n- Valor total: R$ {linha[4]:.2f}")

    conn.close()


# Função para buscar pedido
def search_pedido():
    print("\n=== BUSCAR PEDIDO ===")
    codigo = input("Digite o código do pedido: ").strip()

    conn = sqlite3.connect('collab_notebooks/database/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pedidos WHERE codigo = ?", (codigo,))
    pedido = cursor.fetchone()
    conn.close()

    if pedido:
        print(f"\nPedido encontrado!\nCódigo: {pedido[0]}  \n- Cliente: {pedido[1]} \n- Prato: {pedido[2]} \n- Quantidade: {pedido[3]} \n- Valor total: R$ {pedido[4]:.2f}")
    else:
        print("Pedido não encontrado.")


# Função para atualizar pedido
def update_pedido():
    print("\n=== ATUALIZAR PEDIDO ===")
    codigo = input("Digite o código do pedido para atualizar: ").strip()
    if codigo == "":
        print("Código inválido!")
        return update_pedido()

    print("1. Prato \n2. Quantidade \n3. Valor total \n0. Voltar")
    opcao = input("Escolha uma opção para atualizar: ")

    conn = sqlite3.connect('collab_notebooks/database/database.db')
    cursor = conn.cursor()
        
    if opcao == "1":
        novo_prato = input("Digite o novo prato: ").strip()
        cursor.execute("UPDATE pedidos SET prato = ? WHERE codigo = ?", (novo_prato, codigo))
    elif opcao == "2":
        nova_quantidade = int(input("Digite a nova quantidade: ").strip())
        cursor.execute("UPDATE pedidos SET quantidade = ? WHERE codigo = ?", (nova_quantidade, codigo))
    elif opcao == "3":
        novo_valor = float(input("Digite o novo valor total: ").strip())
        cursor.execute("UPDATE pedidos SET valor_total = ? WHERE codigo = ?", (novo_valor, codigo))
    elif opcao == "0":
        conn.close()
        return
    else:
        print("Opção inválida!")
        conn.close()
        return

    conn.commit()
    conn.close()
    print("Pedido atualizado com sucesso!!!")
    return update_pedido()


# Função para remover pedido
def delete_pedido():
    print("\n=== REMOVER PEDIDO ===")
    codigo = input("Digite o código do pedido para remover: ").strip()

    conn = sqlite3.connect('collab_notebooks/database/database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pedidos WHERE codigo = ?", (codigo,))
    conn.commit()
    conn.close()
    print("Pedido removido com sucesso!!!")
    return

menu()