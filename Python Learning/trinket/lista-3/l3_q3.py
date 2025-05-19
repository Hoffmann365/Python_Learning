# variáveis
total = 0
# funções
def VerificarPrecoProduto(codigo):
    match codigo:
        case 100:
            return 5.50
        case 101:
            return 15
        case 103:
            return 20
        case 104:
            return 18
        case 105:
            return 6
        case _:
            return 0
# entrada
while True:
    codItem = int(input("Digite o código do item: "))
    if codItem == -1:
        break
    else:
        qtdItem = int(input("Digite a quantidade do item: "))

        total += VerificarPrecoProduto(codItem) * qtdItem
# saída
print(f"Total a pagar: R$ {total:.2f}")

    