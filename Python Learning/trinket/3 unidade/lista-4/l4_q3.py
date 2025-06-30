# funções
def validar_n(n):
    return n > 0

def imprimir_triangulo(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()

# entrada
n = int(input("Digite o valor de n: "))

# saída
if validar_n(n):
    imprimir_triangulo(n)
else:
    print("Valor invalido!")
