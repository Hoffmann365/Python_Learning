number = int(input("Digite um número: "))
fatorial = 1

if number > 0:
    for i in range(1, number+1):
        fatorial *= i
        
    print(f"Resultado do fatorial: {fatorial}")
else:
    print("O número deve ser maior que 0.")
