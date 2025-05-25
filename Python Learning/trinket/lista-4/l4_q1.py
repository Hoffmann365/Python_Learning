#lista
listaConvidados = ["Daniel", "Aluizio", "Isabel", "Teles", "Eduardo"]

# variáveis
lengthLista = len(listaConvidados)

# entrada
print("Qual nome você quer verificar? ")
targetName = input()

verifyName = listaConvidados.__contains__(targetName)

print("A lista contém os seguintes nomes: ")
for i in range(lengthLista):
    print(listaConvidados[i])

if verifyName:
    print(f"O nome {targetName} está na lista, acesso permitido!")
elif not verifyName:
    print(f"O nome {targetName} não está na lista, acesso negado!")

