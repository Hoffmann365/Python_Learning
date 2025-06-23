#lista
nomes = []
# entrada
print("Quantos nomes?")
qtdNomes = int(input())
for i in range(qtdNomes):
    nome = input()
    nomes.append(nome)
#saida
print("Você digitou:")
for nome in reversed(nomes): print(nome)