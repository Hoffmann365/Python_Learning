number = int(input("Qual é o número inteiro que deve ser utilizado para gerar a sequência? "))

seq1 = number - 2;
seq2 = number - 1;
seq3 = number;
seq4 = number + 1;
seq5 = number + 2;

total = seq1 + seq2 + seq3 + seq4 + seq5

print(f"A sequência é a seguinte: {seq1} {seq2} {seq3} {seq4} {seq5} {total}")