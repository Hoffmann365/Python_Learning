jogadores = []
totalSaque = totalBloqueio = totalAtaque = 0
acertosSaque = acertosBloqueio = acertosAtaque = 0
# entrada
print("Quantidade de jogadores:")
qtd_jogadores = int(input())
print("Digite os dados para cada jogador:")
for i in range(qtd_jogadores):
    dados = input().split()
    nome = dados[0]
    S = int(dados[1])
    B = int(dados[2])
    A = int(dados[3])
    S1 = int(dados[4])
    B1 = int(dados[5])
    A1 = int(dados[6])
    jogadores.append([S, B, A, S1, B1, A1])

# calculo
for jogador in jogadores:
    totalSaque += jogador[0]
    totalBloqueio += jogador[1]
    totalAtaque += jogador[2]
    acertosSaque += jogador[3]
    acertosBloqueio += jogador[4]
    acertosAtaque += jogador[5]

# descobri como fazer if ternário em python, adianta dms
percentualSaque = (acertosSaque / totalSaque) * 100 if totalSaque > 0 else 0 
percentualBloqueio = (acertosBloqueio / totalBloqueio) * 100 if totalBloqueio > 0 else 0
percentualAtaque = (acertosAtaque / totalAtaque) * 100 if totalAtaque > 0 else 0

# saida
print("As estatísticas do jogo são as seguintes:")
print("Pontos de Saque: {:.2f} %".format(percentualSaque))
print("Pontos de Bloqueio: {:.2f} %".format(percentualBloqueio))
print("Pontos de Ataque: {:.2f} %".format(percentualAtaque))