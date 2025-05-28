# Variáveis
total = 0

# Entrada
qtdItens = int(input("Quantos itens serão calculados? "))

for i in range(qtdItens):
    valorItem = float(input(f"Qual o valor do item {i+1}: "))
    qtdItem = int(input(f"Qual a quantidade do item {i+1}: "))

    total += (valorItem * qtdItem)

# Saída
print(f"O valor total de sua compra: {total:.2f}")