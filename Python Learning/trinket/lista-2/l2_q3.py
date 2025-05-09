numeroPessoas = int(input("Qual o número de pessoas? "))
totalIdades = 0

print("Informe as idades:")

for i in range(numeroPessoas):
    idade = int(input(""))
    totalIdades = totalIdades + idade

mediaIdades = int(totalIdades / numeroPessoas)

print(f"A média de idade das pessoas é {mediaIdades} anos")