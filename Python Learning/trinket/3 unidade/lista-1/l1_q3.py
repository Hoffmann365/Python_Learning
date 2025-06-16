# entrada
temperatura = input().split()
valor = float(temperatura[0])
escala = temperatura[1].upper()

# conversão
if escala == 'C':
    celsius = valor
    fahrenheit = (valor * 9/5) + 32
    kelvin = valor + 273.15
elif escala == 'F':
    celsius = (valor - 32) * 5/9
    fahrenheit = valor
    kelvin = celsius + 273.15
elif escala == 'K':
    kelvin = valor
    celsius = valor - 273.15
    fahrenheit = (celsius * 9/5) + 32
else:
    print("Escala inválida.")
    exit()

# saída
print("Temperatura em Celsius: {:.2f} °C".format(celsius))
print("Temperatura em Fahrenheit: {:.2f} °F".format(fahrenheit))
print("Temperatura em Kelvin: {:.2f} K".format(kelvin))