# Abaixo, segue um código de um dicionário de dados que fará e mostrará o estoque de uma loja de jogos, e os valores respectivos dos jogos que o cliente deseja.

print('Seja Bem Vindo A Simple Store\n')


estoque = {
    "FIFA 23": 199.99,
    "Call of Duty: Warzone": 149.99,
    "Cyberpunk 2077": 99.99,
    "EA FC": 79.99,
    "Grand Theft Auto V": 69.99
}

carrinho = {}

while True:
    print("Produtos disponíveis:")
    for jogo, preco in estoque.items():
        print(f"{jogo}: R${preco:.2f}")

    jogo_desejado = input("\nDigite o nome do jogo que deseja comprar (ou 'sair' para encerrar as compras): ")

    if jogo_desejado.lower() == "sair":
        break

    if jogo_desejado in estoque:
        quantidade = int(input(f"Digite a quantidade de {jogo_desejado} que deseja comprar: "))
        
        if quantidade > 0 and quantidade <= estoque[jogo_desejado]:
            if jogo_desejado in carrinho:
                carrinho[jogo_desejado] += quantidade
            else:
                carrinho[jogo_desejado] = quantidade
            estoque[jogo_desejado] -= quantidade
            print(f"{quantidade} {jogo_desejado} adicionado(s) ao carrinho de compras.")
        else:
            print("Quantidade indisponível em estoque.")
    else:
        print("Jogo não encontrado. Tente novamente.")

print("\nCarrinho de compras:")
total = 0
for jogo, quantidade in carrinho.items():
    preco_unitario = estoque[jogo] + quantidade
    subtotal = quantidade * preco_unitario
    print(f"{jogo}: {quantidade} x R${preco_unitario:.2f} = R${subtotal:.2f}")
    total += subtotal

print(f"Total a pagar: R${total:.2f}")

while carrinho:
    item_remover = input("\nDigite o nome do jogo que deseja remover do carrinho (ou 'continuar' para finalizar a compra): ")
    if item_remover.lower() == "continuar":
        break
    if item_remover in carrinho:
        quantidade_remover = int(input(f"Digite a quantidade de {item_remover} que deseja remover: "))
        if quantidade_remover <= 0:
            print("Quantidade inválida. Tente novamente.")
        elif quantidade_remover <= carrinho[item_remover]:
            carrinho[item_remover] -= quantidade_remover
            estoque[item_remover] += quantidade_remover
            subtotal_remover = quantidade_remover * (estoque[item_remover] + quantidade_remover)
            total -= subtotal_remover
            print(f"{quantidade_remover} {item_remover} removido(s) do carrinho.")
            if carrinho[item_remover] == 0:
                del carrinho[item_remover]
        else:
            print("Quantidade inválida. Tente novamente.")

print("\nRecibo de Compra:")
for jogo, quantidade in carrinho.items():
    preco_unitario = estoque[jogo] + quantidade
    subtotal = quantidade * preco_unitario
    print(f"{jogo}: {quantidade} x R${preco_unitario:.2f} = R${subtotal:.2f}")

print(f"Total a pagar: R${total:.2f}")

print("Obrigado por sua compra!")