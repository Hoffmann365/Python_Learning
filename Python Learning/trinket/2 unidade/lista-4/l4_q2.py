# lista
listaNotas = []

# variaveis
somaNotas = 0

# entrada
print("Digite 10 números:")
for i in range(10):
    nota = int(input())
    somaNotas += nota
    listaNotas.append(nota)

mediaNotas = somaNotas / 10

# saída
print(f"A media é: {mediaNotas}")
print("Os números acima da média são: ")
for i in range(10):
    if listaNotas[i] > mediaNotas:
        print(listaNotas[i])