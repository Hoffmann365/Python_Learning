# Função que verifica se o número é par
def par(n):
    if n % 2 == 0:
        return 0
    else:
        return 1

# Entrada dos 4 números
soma = 0
for i in range(1, 5):
    numero = int(input("Digite número {}: ".format(i)))
    if par(numero) == 0:
        soma += numero

# Saída
print("Soma dos números pares: {}".format(soma))
