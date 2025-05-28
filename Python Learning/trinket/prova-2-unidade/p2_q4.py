# Lista
listaNumeros = []

# Variáveis
somaNumeros = 0

# Entrada
print("Digite 10 números: ")
for i in range(10):
    number = int(input())
    somaNumeros += number
    listaNumeros.append(number)

media = somaNumeros / 10

# Saída
print(f"A média é: {media:.1f}")
print("Os números acima da média são: ")
for i in range(10):
    if listaNumeros[i] > media:
        print(listaNumeros[i])
