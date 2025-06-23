# listas
alunos = []
pares = []
# entrada
print("Quantos alunos?")
qtdAlunos = int(input())
print("Digite os nomes dos alunos:")
for i in range(qtdAlunos):
    nome = input()
    alunos.append(nome)
# troca de lugar
for i in range(qtdAlunos):
    if i % 2 == 1: pares.append(i)

meio = len(pares) // 2

for i in range(meio):
    a = pares[i]
    b = pares[-(i+1)] # indice negativo pra acessar o final da lista (-1 = ultimo elemento)
    alunos[a], alunos[b] = alunos[b], alunos[a]

# saida
print("Nova lista:")
for nome in alunos: print(nome)