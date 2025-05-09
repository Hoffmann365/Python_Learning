nome = input("Qual o nome do candidato? ")
idade = int(input("Qual a idade do candidato? "))

if idade < 5:
    print("Categoria não aplicável para menores de 5 anos.")
elif idade > 25:
    print("Fora das categorias estabelecidas.")
elif idade >= 5 and idade <= 10:
    print(f"O atleta {nome} está classificado na categoria Infantil.")
elif idade >= 11 and idade <= 15:
    print(f"O atleta {nome} está classificado na categoria Juvenil.")
elif idade >= 16 and idade <= 20:
    print(f"O atleta {nome} está classificado na categoria Junior.")
elif idade >= 21 and idade <= 25:
    print(f"O atleta {nome} está classificado na categoria Profissional.")