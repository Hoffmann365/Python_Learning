# variáveis
somaIdades = 0

# entrada
print("Qual o número de pessoas?")
peopleNumber = int(input())

print("Informe as idades: ")
for i in range(peopleNumber):
    idade = int(input())
    somaIdades += idade

mediaIdades = int(somaIdades / peopleNumber)

print(f"A média de idade das pessoas é {mediaIdades} anos")