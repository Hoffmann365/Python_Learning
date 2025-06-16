distancia = float(input("Qual é a distância da viagem de ida e volta em quilômetros? "))
consumo = float(input("Quantos quilômetros o carro percorre com cada litro de combustível? "))
preço = float(input("Qual é o preço em reais por litro de combustível? 200.0 "))

valor = (distancia / consumo) * preço

print(f"O valor em reais para realizar a viagem pretendida é {valor:.2f}")