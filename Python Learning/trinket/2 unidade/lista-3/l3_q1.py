alturaInicialLevi = float(input("Qual a altura inicial de Levi? "))
taxaCrescLevi = float(input("Qual a taxa de crescimento de Levi? "))

alturaInicialHiago = float(input("Qual a altura incial de Hiago? "))
taxaCrescHiago = float(input("Qual a taxa de crescimento inicial de Hiago? "))

if alturaInicialHiago > alturaInicialLevi and taxaCrescLevi > taxaCrescHiago:
    numAnos = int(abs((alturaInicialHiago - alturaInicialLevi) / ((taxaCrescLevi/100) - (taxaCrescHiago/100))))

    print(f"Serão necessários {numAnos} anos para que Levi seja maior que Hiago.")
if alturaInicialLevi >= alturaInicialHiago:
    print("Erro: Hiago deve ser maior que Levi inicialmente.")
if taxaCrescHiago >= taxaCrescLevi:
    print("Erro: A taxa de crescimento de Levi deve ser maior que a de Hiago.")
