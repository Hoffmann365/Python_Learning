valorMulta = float(input("Qual é o valor original cobrado por cada multa? "))
juros = float(input("Qual é a porcentagem de juros cobrada pelo Detran? "))
amigos = int(input("Quantos amigos irão contribuir com as despesas? "))

valorPagamento = ((valorMulta * 2) * (1.00 +(juros / 100))) / amigos

print(f"O valor em reais que cada amigo deverá pagar ao Detran é {valorPagamento:.2f}")