# entrada pt.1
N = int(input())

for _ in range(N):
    # entrada pt.2
    par = input().split()
    X = int(par[0])
    Y = int(par[1])

    # calculo
    if X % 2 == 0:
        X += 1
    
    soma = 0
    for i in range(Y):
        soma += X + i * 2

    # saida
    print(soma)