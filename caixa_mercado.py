# entrada de produtos
def registraProd():
    registraCompra = {}
    indicaOperacao = True
    while indicaOperacao:
        operacao = input("Pressione A para adicionar o produto e Q para encerrar: ")
        if operacao == "A":
            produto = input("Registre o produto: ")
            quantidade = int(input("Entre a quantidade: "))
            registraCompra[produto] = quantidade  # Armazena produto e quantidade
        elif operacao == "Q":
            indicaOperacao = False
        else:
            print("Por favor, indique a opção correta(A ou Q):")
    return registraCompra


def buscaPreco(produto, quantidade):  # Corrigido os parâmetros
    precoProduto = {
        'Biscoito': 3.5,
        'Frango': 18.99,
        'Ovos': 1.02,
        'Peixe': 33.45,
        'Refri': 8.78,
        'Pão': 7.59,
        'Maçã': 14.75,
        'Cebola': 3.46,
    }
    preco = precoProduto.get(produto, 0)  # Busca o preço do produto
    subtotal = preco * quantidade
    print(produto + ':R$ ' +
          str(preco) + 'x' + str(quantidade) + '=' + str(subtotal))
    return subtotal


def geraDesconto(totalFatura, modalidade):
    desconto = 0
    if totalFatura >= 25:
        if modalidade == 'Gold':
            desconto = 30  # Corrigido para 30% conforme a operação abaixo
            totalFatura = totalFatura * 0.70  # 30% de desconto = pagar 70%
        elif modalidade == 'Silver':
            desconto = 20  # Corrigido para 20% conforme a operação abaixo
            totalFatura = totalFatura * 0.80  # 20% de desconto = pagar 80%
        elif modalidade == 'Bronze':
            desconto = 5
            totalFatura = totalFatura * 0.95  # 5% de desconto = pagar 95%
        print(str(desconto) + "% de desconto para modalidade " + modalidade +
              ", no valor de: R$ " + str(totalFatura))
    else:
        print("Sem desconto para total abaixo de R$ 25,00")
    return totalFatura


def geraFatura(registraCompra, modalidade):
    totalFatura = 0
    for produto, quantidade in registraCompra.items():  # Corrigido para pegar produto e quantidade
        totalFatura += buscaPreco(produto, quantidade)
    totalFatura = geraDesconto(totalFatura, modalidade)
    print("O valor total é: R$ " + str(totalFatura))


registraCompra = registraProd()
modalidade = input("Indique a modalidade do cliente: ")
geraFatura(registraCompra, modalidade)