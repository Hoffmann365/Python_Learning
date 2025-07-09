# entrada
N = int(input("Digite um número inteiro positivo: "))


# saida
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  

# A melhor forma de estruturar a lógica deste programa é usar dois laços de repetição:
# um laço externo para controlar as linhas (de 1 até N),
# e um laço interno para imprimir os números de 1 até o número da linha atual.
# Isso funciona bem porque o padrão é incremental e previsível,
# e a cada linha o número de elementos cresce em +1.
# Como não precisamos armazenar os dados, evitamos listas e strings complexas,
# focando apenas na lógica de repetição e na impressão ordenada.