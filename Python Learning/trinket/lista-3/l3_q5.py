lista_gastos = []

print("Informe os gastos no dia: ")
while True:
    gasto = float(input())
    if gasto == 0:
        break
    lista_gastos.append(gasto)

print(lista_gastos)
if lista_gastos == []:
    print("Você não teve gastos hoje!")
else:
    maiorGasto = max(lista_gastos)
    print(f"O seu maior gasto hoje foi: R$ {maiorGasto:.2f}")
