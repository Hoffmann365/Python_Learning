while True:
    N = int(input())
    if N == 0:
        break

    for i in range(N):
        for j in range(N):
            valor = abs(i - j) + 1
            # Alinha à direita com largura 3
            if j == 0:
                print("{:>3}".format(valor), end='')
            else:
                print(" {:>3}".format(valor), end='')
        print()
    print()
