pedidos = []
codigo_id = 1

def menu():
    global codigo_id
    while True:
        print("\n===== SISTEMA CONN =====")
        print("1 - Cadastrar pedido")
        print("2 - Listar pedidos")
        print("3 - Buscar pedido")
        print("4 - Atualizar pedido")
        print("5 - Remover pedido")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            creat_pedido()

        elif opcao == "2":
            list_pedidos()

        elif opcao == "3":
            cod = int(input("Digite o código: "))
            pedido = buscar_pedido(cod)
            if pedido:
                print("Pedido encontrado:", pedido)
            else:
                print("Pedido não encontrado.")

        elif opcao == "4":
            update_pedido()

        elif opcao == "5":
            remove_pedido()

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


## Função Criar Pedido
def creat_pedido():
    global codigo_id
    print("\n=== CADASTRAR PEDIDO ===")
    cliente = input("Cliente: ")
    if cliente.isdigit():
        print("Nome Inválido!")
        return creat_pedido()
    elif not cliente:
        print("Campo Vazio...")
        return creat_pedido()
    # for i in cliente:
    #     Full_Name = i.split() 
    #     len(Full_Name)
    # if len(Full_Name) == 1:
    #     print("Insira o nome completo!")
    #     return creat_pedido()
    prato = input("Prato: ")
    if prato.isdigit():
        print("Prato inválido!")
        return creat_pedido()
    elif not prato:
        print("Informação inválido!")
        return creat_pedido()
    
    quantidade = int(input("Quantidade: "))
    if quantidade == 0:
        print("Campo vazio!:")
        return creat_pedido()
    valor = float(input("Valor total: "))

    pedidos.append({
        "codigo_id": codigo_id,
        "cliente": cliente,
        "prato": prato,
        "quantidade": quantidade,
        "valor": valor
    })
    codigo_id += 1
    print("Pedido cadastrado!")

# Função listar pedidos
def list_pedidos():
    global pedidos
    print("\n=== LISTA DE PEDIDOS ===")
    if not pedidos:
        print("Nenhum pedido cadastrado.")
    else:
        for p in pedidos: # p é cada parte dos pedidos
            print(f"\nCódigo: {p['codigo_id']}") 
            print(f"\nCliente: {p['cliente']} \nPrato: {p['prato']} \nQuantidade: {p['quantidade']} \nValor: R$ {p['valor']:.2f}")

##### Função buscar pedido#####
#def buscar_pedido(cod):
#    cod = int(input("Digite o código: "))
#
#    for p in pedidos:
#        if p["codigo_id"] == cod:
#            print(f"Pedido encontrado: {p}")
#        else:
#            print("Pedido não encontrado.")
#    return

def buscar_pedido(cod):
    for p in pedidos:   # motor de busca
        if p["codigo_id"] == cod:
            return p
    return None

# Função atualizar pedido
def update_pedido():
    global pedidos
    print("\n=== ATUALIZAR PEDIDO ===")
    cod = int(input("Digite o código: "))
    pedido = buscar_pedido(cod)
    if pedido:
        pedido["prato"] = input("Novo prato: ")
        pedido["quantidade"] = int(input("Nova quantidade: "))
        pedido["valor"] = float(input("Novo valor: "))
        print("Pedido atualizado!")
    else:
        print("Pedido não encontrado.")

# Função remover pedido
def remove_pedido():
    global pedidos
    print("\n=== REMOVER PEDIDO ===")
    print(pedidos)
    cod = int(input("Digite o código: "))
    #pedidos[:] = [p for p in pedidos if p["codigo_id"] != cod]
    if pedidos == []:
        print("Nenhum pedido cadastrado.")
        return menu()
    elif cod > len(pedidos):
        print("Código inválido!")
        return remove_pedido()
    elif cod == "":
        print("Nada informado, retornando!")
        return remove_pedido()
    
    pedidos = [p for p in pedidos if p["codigo_id"] != cod]
    print("Pedido removido!")

menu()