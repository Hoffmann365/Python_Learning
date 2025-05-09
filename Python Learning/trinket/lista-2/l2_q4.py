peso = float(input("Informe o peso (Kg): "))
altura = float(input("Informe a altura(m): "))

imc = peso / (altura * altura)

print(imc)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso Normal")
elif imc >= 25 and imc <=29.9:
    print("Sobrepeso")
elif imc >= 30.0:
    print("Obesidade")