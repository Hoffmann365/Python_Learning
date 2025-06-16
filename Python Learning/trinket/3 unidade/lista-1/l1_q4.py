# entrada
valores = input().split()

# conversão pra int
x1 = int(valores[0])
y1 = int(valores[1])
x2 = int(valores[2])
y2 = int(valores[3])
px = int(valores[4])
py = int(valores[5])

# garante a ordem dos valores no par
xmin = min(x1, x2)
xmax = max(x1, x2)
ymin = min(y1, y2)
ymax = max(y1, y2)

# saída
if xmin <= px <= xmax and ymin <= py <= ymax:
    print("Dentro!")
else:
    print("Fora!")