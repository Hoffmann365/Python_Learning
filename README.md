# Anotações

# Conceitos Básicos e Sintaxe

### Identação

Diferente de outras linguagens que utilizam chaves ou palavras-chave, o Python utiliza a indentação para determinar o escopo das declarações.  
Ex:
```python
if condition:

    # Bloco de código se a condição for verdadeira

    instrucao1
    instrucao2

else:

    # Bloco de código se a condição for falsa

    instrucao3
    instrucao4
```

### Comentários

Em Python os comentários de linha única começam com #, e os de várias linhas ficam entre 3 aspas duplas (""")  
Ex:
```Python
# Este é um comentário de uma única linha

"""
Este é um comentário
de várias linhas
"""
```

### Maiúsculas e minúsculas

Python distingue entre maiúsculas e minúsculas. Portanto, variável, Variável e VARIÁVEL são consideradas variáveis diferentes.

### Ponto e Vírgula

Python não requer o uso de ponto e vírgula (;) ao final de cada instrução. No entanto, se você desejar escrever várias instruções em uma única linha, pode separá-las com um ponto e vírgula.   
Ex:
```python
instrucao1; instrucao2; instrucao3
```

### Uso de Parênteses

Os parênteses são utilizados para agrupar expressões, definir funções e realizar chamadas a funções.  
Ex:
```python
resultado = (a + b) * c
```

# Tipos de dados básicos
Em Python, os tipos de dados básicos são as categorias nas quais podemos classificar os valores que utilizamos em nossos programas.  

* **Inteiros(int)**

Os números inteiros são aqueles que não têm parte decimal. Em Python, são representados simplesmente escrevendo o número sem aspas nem pontos decimais.  
Ex:
```python
idade = 25
quantidade = 100
```
* **Flutuantes(float)**

Os números flutuantes, também conhecidos como números de ponto flutuante, são aqueles que têm uma parte decimal. Em Python, são representados utilizando um ponto para separar a parte inteira da parte decimal.  
Ex:
```python
preço = 9.99
altura = 1.75
```

* **Cadeias de Texto(Strings)**

As cadeias de texto, ou simplesmente cadeias, são sequências de caracteres encerradas entre aspas simples ('...') ou duplas ("..."). São utilizadas para representar texto em Python.  
Ex:
```python
nome = "Juan"
mensagem = '¡Hola, mundo!'
```

* **Booleanos**

Os valores booleanos representam os valores de verdade: True (verdadeiro) e False (falso). São comumente utilizados em expressões condicionais e operações lógicas.  
Ex:
```python
é maior de idade = True
tem desconto = False
```
**Obs:** Os valores booleanos em Python começam com uma letra maiúscula: True e False.  

# Variáveis

### Declaração e atribuição de variáveis
As variáveis são contêineres que nos permitem armazenar e manipular dados em nossos programas. Para declarar e atribuir um valor a uma variável em Python, utilizamos o operador de atribuição =. O nome da variável vai à esquerda do operador, e o valor que você deseja atribuir vai à direita.  
Ex:
```python
nome = "Juan"
idade = 25
altura = 1.75
é estudante = True
```
O Python infere automaticamente o tipo de dados de cada variável com base no valor atribuído.
Você também pode atribuir o mesmo valor a várias variáveis em uma única linha usando o operador de atribuição múltipla:
```python
a = b = c = 10
```

### Regras para nomear variáveis
Ao nomear variáveis em Python, é importante seguir algumas regras para manter um código legível e evitar erros:
>Os nomes das variáveis só podem conter letras (a-z, A-Z), números (0-9) e
>sublinhados (_). Não podem começar com um número.

>Não se pode usar palavras-chave reservadas do Python como nomes de
>variáveis (por exemplo, if, else, for, while, etc.).

>O Python diferencia maiúsculas de minúsculas, então nome e Nome são
>variáveis diferentes.

>Recomenda-se usar nomes descritivos para as variáveis, que indiquem
>claramente seu propósito: nome, idade, total_vendas, etc.

# Operadores

### Aritméticos
Os operadores aritméticos são utilizados para realizar operações matemáticas básicas. Os principais operadores aritméticos em Python são:

* Soma (+): soma dois valores.
* Subtração (-): subtrai o segundo valor do primeiro.
* Multiplicação (*): multiplica dois valores.
* Divisão (/): divide o primeiro valor pelo segundo e devolve um resultado de tipo flutuante.
* Divisão inteira (//): divide o primeiro valor pelo segundo e devolve um resultado de tipo inteiro (a parte decimal é descartada).
* Módulo (%): devolve o resto da divisão entre o primeiro valor e o segundo.
* Exponenciação (**): eleva o primeiro valor à potência do segundo.  

Ex: 
```python
a = 10
b = 3


soma = a + b   # 13
subtracao = a - b    # 7
multiplicacao = a * b    # 30
divisao = a / b   # 3.333333333
divisao_inteira = a // b   # 3
modulo = a % b   # 1
exponenciacao = a ** b   # 1000
```
### De comparação
Os operadores de comparação são utilizados para comparar dois valores e devolvem um valor booleano (True ou False) segundo o resultado da comparação. Os operadores de comparação em Python são:

* Igual a (==): devolve True se ambos os valores são iguais.
* Diferente de (!=): devolve True se os valores são diferentes.
* Maior que (>): devolve True se o primeiro valor é maior que o segundo.
* Menor que (<): devolve True se o primeiro valor é menor que o segundo.
* Maior ou igual que (>=): devolve True se o primeiro valor é maior ou igual que o segundo.
* Menor ou igual que (<=): devolve True se o primeiro valor é menor ou igual que o segundo.  

Ex:  
```python
a = 10
b = 3


igual = a == b   # False
diferente = a != b   # True
maior que = a > b   # True
menor que = a < b   # False
maior ou igual = a >= b   # True
menor ou igual = a <= b   # False
```

### Lógicos
Os operadores lógicos são utilizados para combinar expressões condicionais e avaliar múltiplas condições. Os operadores lógicos em Python são:

* AND (and): devolve True se ambas as condições são verdadeiras.
* OR (or): devolve True se ao menos uma das condições é verdadeira.
* NOT (not): inverte o valor de uma condição, devolve True se a condição é falsa e False se a condição é verdadeira.  

Ex:
```python
a = 10
b = 3


resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False
```
**OBS:** Python segue as regras de precedência de operadores, onde certos operadores têm prioridade sobre outros. Em geral, a precedência segue a ordem: parênteses, exponenciação, multiplicação/divisão, soma/subtração, operadores de comparação e operadores lógicos.

# Estruturas de Controle
As estruturas de controle nos permitem controlar o fluxo de execução de nossos programas. Em Python, as estruturas de controle mais comuns são as estruturas condicionais e os loops. Essas estruturas nos permitem tomar decisões e repetir blocos de código segundo certas condições.

### Estruturas Condicionais
As estruturas condicionais nos permitem executar diferentes blocos de código segundo se cumpra ou não uma determinada condição. Em Python, as estruturas condicionais mais utilizadas são if, if-else e if-elif-else.

* **IF**

A estrutura if é utilizada para executar um bloco de código se uma condição for verdadeira. A sintaxe básica é a seguinte:
```python
if condicao:

   # Bloco de código a executar se a condição for verdadeira
   instruções
```
Exemplo:
```python
idade = 18


if idade >= 18:
   print ("Você é maior de idade.")
```

* **IF-ELSE**

A estrutura if-else nos permite especificar um bloco de código alternativo que será executado se a condição do if for falsa. A sintaxe básica é a seguinte:
```python
idade = 15


if idade >= 18:
   print ("Você é maior de idade.")

else:
   print ("Você é menor de idade.")
```
Neste exemplo, se a variável idade for maior ou igual a 18, será executado o bloco de código dentro do if e será impressa a mensagem "Você é maior de idade." Caso contrário, será executado o bloco de código dentro do else e será impressa a mensagem "Você é menor de idade."

* **IF-ELIF-ELSE**

A estrutura if-elif-else nos permite especificar múltiplas condições e blocos de código alternativos. A sintaxe básica é a seguinte:
```python
if condicao1:

   # Bloco de código a executar se a condicao1 for verdadeira
   instruções

elif condicao2:

   # Bloco de código a executar se a condicao2 for verdadeira
   instruções

else:

   # Bloco de código a executar se nenhuma condição anterior for verdadeira
   instruções
```
Exemplo:
```python
nota = 85


if nota >= 90:
   print ("Excelente")

elif nota >= 80:
   print ("Muito bom")

elif nota >= 70:
   print ("Bom")

else:
   print ("Precisa melhorar")
```
Neste exemplo, são avaliadas múltiplas condições em ordem. Se a variável nota for maior ou igual a 90, será impresso "Excelente". Se não se cumprir a primeira condição, mas nota for maior ou igual a 80, será impresso "Muito bom". Se não se cumprirem as condições anteriores, mas nota for maior ou igual a 70, será impresso "Bom". Se nenhuma das condições anteriores for verdadeira, será executado o bloco else e será impresso "Precisa melhorar".

# Loops
Os loops nos permitem repetir um bloco de código várias vezes. Em Python, os loops mais comuns são for e while.

### For
O loop for é utilizado para iterar sobre uma sequência (como uma lista, uma tupla ou uma string) ou qualquer objeto iterável. A sintaxe básica é a seguinte:
```python
for variável in sequência:

    # Bloco de código a repetir
    instruções
```
Exemplo:
```python
frutas = ["maçã", "banana", "laranja"]


for fruta in frutas:
    print(fruta)
```
Neste exemplo, o loop for itera sobre a lista frutas. Em cada iteração, a variável fruta assume o valor de um elemento da lista, e o bloco de código dentro do loop é executado. Neste caso, cada fruta é impressa em uma linha separada.

### While
O loop while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira. A sintaxe básica é a seguinte:
```python
while condição:

    # Bloco de código a repetir
    instruções
```
Exemplo:
```python
contador = 0


while contador < 5:

    print(contador)
    contador += 1
```
Neste exemplo, o loop while é executado enquanto a variável contador for menor que 5. Em cada iteração, o valor de contador é impresso e depois incrementado em 1 pela instrução contador += 1. O loop será interrompido quando contador atingir o valor de 5.

É importante ter cuidado ao usar o loop while, pois, se a condição nunca se tornar falsa, o loop será executado indefinidamente, o que é conhecido como um loop infinito.

### Controle de Loops
Python fornece algumas instruções especiais para controlar o fluxo de execução dentro dos loops:

* **Break**

A instrução break é utilizada para sair prematuramente de um loop, independentemente da condição. Quando um break é encontrado, o loop é interrompido e o fluxo de execução continua com a próxima instrução fora do loop.
```python
contador = 0


while True:

    print(contador)
    contador += 1


    if contador == 5:
        break
```
Neste exemplo, o loop while é executado indefinidamente devido à condição True. No entanto, dentro do loop é utilizada uma estrutura condicional if para verificar se contador é igual a 5. Quando essa condição é satisfeita, a instrução break é executada, fazendo com que o loop seja interrompido e o fluxo de execução continue com a próxima instrução fora do loop.

* **Continue**

A instrução continue é utilizada para pular o restante do bloco de código dentro de um loop e passar para a próxima iteração.  

Exemplo:
```python
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)
```
Neste exemplo, o loop for itera sobre os números de 0 a 9 utilizando a função range(). Dentro do loop, verifica-se se o número é divisível por 2 utilizando o operador de módulo %. Se o número for divisível por 2 (ou seja, se for par), a instrução continue é executada, fazendo com que o restante do bloco de código seja pulado e passando para a próxima iteração do loop. Como resultado, apenas os números ímpares serão impressos.

* **Pass**

A instrução pass é uma operação nula que não faz nada. É utilizada como um marcador de posição quando uma instrução é sintaticamente necessária, mas nenhuma ação é desejada.

Exemplo:
```python
for i in range(5):
    pass
```
Neste exemplo, o loop for itera sobre os números de 0 a 4, mas nenhuma ação é realizada dentro do loop devido à instrução pass. Isso pode ser útil quando se está desenvolvendo um programa e se deseja reservar um bloco de código para implementá-lo mais tarde.



```python

```
