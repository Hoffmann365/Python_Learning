# entradas
print("Qual a nota da primeira unidade?")
nota1 = float(input())
print("Qual a nota da segunda unidade?")
nota2 = float(input())
print("Qual a nota da terceira unidade?")
nota3 = float(input())

def CalcularMedia(n1, n2, n3):
    media = ((n1 * 2) + (n2 * 3) + (n3 * 4)) / 9
    if media >= 7:
        print("Francisco está aprovado")
    elif media < 7 and media > 3:
        print("Francisco está em prova final")
    elif media <= 3:
        print("Francisco está reprovado")

CalcularMedia(nota1, nota2, nota3)
