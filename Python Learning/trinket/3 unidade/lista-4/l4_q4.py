# funções
def inverter_numero(n):
    n_str = str(n)
    n_invertido = n_str[::-1]
    return n_invertido

# entrada
numero = int(input("Digite um valor: "))

inverso = inverter_numero(numero)

# saída
print("Inverso: {}".format(inverso))
