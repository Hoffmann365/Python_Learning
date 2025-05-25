# lista
listaMeses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# entrada
print("Qual o número do mês?")
targetMonth = int(input())

if targetMonth >= 1 and targetMonth <= 12:
    print(f"O mês é {listaMeses[targetMonth-1]}")
else:
    print(f"Erro: não existe mês de número {targetMonth}! Por favor, digite um número entre 1 e 12.")