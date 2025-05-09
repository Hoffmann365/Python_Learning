nota1 = float(input("Qual é a nota da primeira unidade? "))
nota2 = float(input("Qual é a nota da segunda unidade? "))
nota3 = float(input("Qual é a nota da terceira unidade? "))

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4)) / (2 + 3 + 4)

if media >= 7:
    print("Francisco está aprovado")
elif media < 3:
    print("Francisco está reprovado")
else:
    print("Francisco está em prova final")