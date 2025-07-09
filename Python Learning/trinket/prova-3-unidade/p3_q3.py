import random

# escolhas
options = ["pedra", "papel", "tesoura"]

# variaveis
playerWins = 0
computerWins = 0

print("Jogo: Pedra, Papel ou Tesoura")
print("Digite 'sair' para encerrar o jogo")

while True:
    player = input("Sua jogada: ").lower()

    if player == "sair":
        print("Jogo encerrado!")
        break

    computer = random.choice(options)
    print("Computador jogou:", computer)

    if player == computer: resultado = "Empate!"
    elif (player == 'pedra' and computer == 'tesoura') or \
         (player == 'papel' and computer == 'pedra') or \
         (player == 'tesoura' and computer == 'papel'):
        resultado = "Você ganhou!"
        playerWins += 1
    else:
        resultado = "Você perdeu!"
        computerWins += 1

    print(resultado)
    print("Placar: Você: {} | Computador: {}\n".format(playerWins, computerWins))