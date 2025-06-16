#variáveis
valorPagar = 0
# entradas
print("Qual o valor da compra? ")
valorCompra = float(input())
print("Como gostaria de pagar: à vista (V) ou a prazo (P)?")
formaPagamento = input()

# saídas
if formaPagamento == "V":
    valorPagar = valorCompra * 0.95
    print(f"Valor à pagar: {valorPagar:.2f}")
elif formaPagamento == "P":
    valorPagar = valorCompra * 1.08
    print(f"Valor à pagar: {valorPagar:.2f}")
    print(f"Parcela 1: {valorPagar/3:.2f}")
    print(f"Parcela 2: {valorPagar/3:.2f}")
    print(f"Parcela 3: {valorPagar/3:.2f}")
else:
    print("Forma de pagamento inválida")