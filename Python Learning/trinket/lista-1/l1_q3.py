widthLote1 = float(input("Qual é a largura do lote 1? "))
lengthLote1 = float(input("Qual é o comprimento do lote 1? "))
widthLote2 = float(input("Qual é a largura do lote 2? "))
lengthLote2 = float(input("Qual é o comprimento do lote 2? "))
widthLote3 = float(input("Qual é a largura do lote 3? "))
lengthLote3 = float(input("Qual é o comprimento do lote 3? "))
widthLote4 = float(input("Qual é a largura do lote 4? "))
lengthLote4 = float(input("Qual é o comprimento do lote 4? "))

areaTotal = (widthLote1 * lengthLote1) + (widthLote2 * lengthLote2) + (widthLote3 * lengthLote3) + (widthLote4 * lengthLote4)

print(f"A área total do terreno é {areaTotal:.2f} m2")