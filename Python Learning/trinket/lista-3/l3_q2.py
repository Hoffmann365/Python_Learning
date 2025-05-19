lista_valores = []
# entrada
print("Insira a taxa do exame para 10 pacientes")
for i in range(10):
    valor = int(input())
    lista_valores.append(valor)
# funções
def MediaAritmetica(lista_numeros):
    soma_valores = 0
    num_valores = len(lista_numeros)

    for numero in lista_numeros:
        soma_valores += numero

    return soma_valores / num_valores
    
def MediaGeometrica(lista_numeros):
    prod_valores = 1
    num_valores = len(lista_numeros)
    for numero in lista_numeros:
        prod_valores *= numero

    return prod_valores ** (1/num_valores)

def MediaHarmonica(lista_numeros):
    soma_inversos = 0
    num_valores = len(lista_numeros)

    for numero in lista_numeros:
        soma_inversos += 1 / numero

    return num_valores / soma_inversos

def ErroMedio(mediaAritmetica, mediaGeometrica, mediaHarmonica):
    erroHarmonica = (mediaHarmonica - mediaAritmetica) / mediaAritmetica
    erroGeometrica = (mediaGeometrica - mediaAritmetica) / mediaAritmetica

    return ((erroHarmonica + erroGeometrica) / 2) * 100
# saída
mediaA = MediaAritmetica(lista_valores)
mediaG = MediaGeometrica(lista_valores)
mediaH = MediaHarmonica(lista_valores)
erroM = ErroMedio(mediaA, mediaG, mediaH)

print(f"Média aritmética: {mediaA:.2f}")
print(f"Média harmônica: {mediaH:.2f}")
print(f"Média geométrica: {mediaG:.2f}")
print(f"Erro médio: {erroM:.2f}%")


