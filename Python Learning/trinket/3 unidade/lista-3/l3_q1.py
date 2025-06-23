lista_valores = []

# entrada
print("Qual o N?")
N = int(input())
print("Digite os valores:")
for i in range(N):
    valor = int(input())
    lista_valores.append(valor)
print("Qual a op?")
OP = int(input())
print("Qual o A?")
A = int(input())
print("Qual o B?")
B = int(input())

# saída
if OP == 0:
    print(f"{lista_valores[A-1]} + {lista_valores[B-1]} = {lista_valores[A-1] + lista_valores[B-1]}")
elif OP == 1:
    print(f"{lista_valores[A-1]} * {lista_valores[B-1]} = {lista_valores[A-1] * lista_valores[B-1]}")