# lista
listaPontuacao = []

# entradas
print("Informe as pontuações dos atletas. Digite -1 para encerrar")
while True:
    value = int(input())
    if value == -1:
        break
    listaPontuacao.append(value)

maiorValor = max(listaPontuacao)

print(f"O recorde de pontos é {maiorValor}.")