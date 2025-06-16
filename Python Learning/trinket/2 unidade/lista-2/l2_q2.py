valor = int(input("Qual o valor da compra? "))
formaDePagamento = input("Como gostaria de pagar à vista(V) ou à prazo (P)? ")
valorFinal = 0

if formaDePagamento == "P":
    valorFinal = int(valor * 1.08)
    parcela = int(valorFinal / 3)
    print(f"Valor à pagar: {valorFinal:}")
    print(f"Parcela 1: {parcela}")
    print(f"Parcela 2: {parcela}")
    print(f"Parcela 3: {parcela}")
elif formaDePagamento == "V":
    valorFinal = int(valor * 0.95)
    print(f"Valor à pagar: {valorFinal}")
else:
    print("Forma de pagamento inválida")