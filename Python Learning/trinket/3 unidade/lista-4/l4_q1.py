# funções
def divisores(n):
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

# entrada
print("Qual o valor de N?")
N = int(input())

numeros = []
print("Digite os valores:")
for i in range(N):
    valor = int(input())
    numeros.append(valor)

# saída
print("A classificação é:")
for num in numeros:
    divs = divisores(num)
    if len(divs) == 2:
        print("{} é primo".format(num))
    else:
        print("{} não é primo, os divisores são: {}".format(num, divs))
