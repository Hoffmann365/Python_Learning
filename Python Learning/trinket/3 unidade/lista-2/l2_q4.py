# entrada pt.1
T = int(input())

for _ in range(T):
    # entrada pt.2
    entrada = input().split()
    PA = int(entrada[0])
    PB = int(entrada[1])
    G1 = float(entrada[2])
    G2 = float(entrada[3])

    # calculo
    anos = 0
    while PA <= PB and anos <= 100:
        PA += int(PA * G1 / 100)
        PB += int(PB * G2 / 100)
        anos += 1

    # saída
    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{anos} anos.")
