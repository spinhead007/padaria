# Dicionários para Comidas e Bebidas
comida = {
    1: {'nome': 'Bolo de cenoura', 'preco': 1.00},
    2: {'nome': 'Sonho', 'preco': 1.10},
    3: {'nome': 'Pão de Mel', 'preco': 1.15},
    4: {'nome': 'Bolo de Morango', 'preco': 2.00},
    5: {'nome': 'Torta Salgada', 'preco': 1.00},


}

bebida = {
    1: {'nome': 'Suco de Uva', 'preco': 1.00},
    2: {'nome': 'Suco de Laranja', 'preco': 1.00},
    3: {'nome': 'Chá de Salvia', 'preco': 1.50},
    4: {'nome': 'Café com Leite', 'preco': 2.50},


}

# Função para exibir o menu de comida
def mostrar_menu_comidas():
    print('Comidas:')
    for key, value in comida.items():
        print(f'{key}-{value["nome"]} = {value["preco"]:.2f}')

# Função para exibir o menu de bebida
def mostrar_menu_bebidas():
    print('Munições:')
    for key, value in bebida.items():
        print(f'{key}-{value["nome"]} = {value["preco"]:.2f}')

# Função para calcular o valor total do pedido
def calcular_valor_total(pedido):
    total = 0
    for item in pedido:
        if item['tipo'] == 'comida':
            total += comida[item['id']]['preco'] * item['quantidade']
        elif item['tipo'] == 'bebida':
            total += bebida[item['id']]['preco'] * item['quantidade']
    return total

# Lista para armazenar o pedido do cliente
pedido = []

# Loop para o menu principal
while True:
    print('--- Menu ---')
    print('1. Adicionar Produto ao pedido')
    print('2. Adicionar Bebidas ao pedido')
    print('3. Remover item do pedido')
    print('4. Ver valor do pedido')
    print('5. Sair')

    escolha = int(input('Escolha uma opção: '))

    if escolha == 1:
        mostrar_menu_comidas()
        comida_id = int(input('Escolha uma Comida (pelo número): '))
        quantidade = int(input('Quantidade desejada: '))
        pedido.append({'id': comida_id, 'tipo': 'comida', 'quantidade': quantidade})
    elif escolha == 2:
        mostrar_menu_bebidas()
        bebida_id = int(input('Escolha uma bebida (pelo número): '))
        quantidade = int(input('Quantidade desejada: '))
        pedido.append({'id': bebida_id, 'tipo': 'bebida', 'quantidade': quantidade})
    elif escolha == 3:
        print('--- Remover Item ---')
        for index, item in enumerate(pedido):
            tipo_item = 'comida' if item['tipo'] == 'comida' else 'bebida'
            nome_item = comida[item['id']]['nome'] if tipo_item == 'comida' else bebida[item['id']]['nome']
            print(f'{index+1}. {nome_item}, Quantidade: {item["quantidade"]}')

        if pedido:
            item_remover = int(input('Escolha um item para remover (pelo número): ')) - 1
            if 0 <= item_remover < len(pedido):
                pedido.pop(item_remover)
            else:
                print('Escolha inválida. Tente novamente.')
        else:
            print('Pedido vazio. Nada para remover.')

    elif escolha == 4:
        total_pedido = calcular_valor_total(pedido)
        print(f'Valor total do pedido: R${total_pedido:.2f}')
    elif escolha == 5:
        break
    else:
        print('Opção inválida. Tente novamente.')

print('Obrigado por comprar na Padaria Pecado da Gula!')