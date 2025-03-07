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

- **Inteiros(int)**

Os números inteiros são aqueles que não têm parte decimal. Em Python, são representados simplesmente escrevendo o número sem aspas nem pontos decimais.  
Ex:

```python
idade = 25
quantidade = 100
```

- **Flutuantes(float)**

Os números flutuantes, também conhecidos como números de ponto flutuante, são aqueles que têm uma parte decimal. Em Python, são representados utilizando um ponto para separar a parte inteira da parte decimal.  
Ex:

```python
preço = 9.99
altura = 1.75
```

- **Cadeias de Texto(Strings)**

As cadeias de texto, ou simplesmente cadeias, são sequências de caracteres encerradas entre aspas simples ('...') ou duplas ("..."). São utilizadas para representar texto em Python.  
Ex:

```python
nome = "Juan"
mensagem = '¡Hola, mundo!'
```

- **Booleanos**

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

> Os nomes das variáveis só podem conter letras (a-z, A-Z), números (0-9) e
> sublinhados (\_). Não podem começar com um número.

> Não se pode usar palavras-chave reservadas do Python como nomes de
> variáveis (por exemplo, if, else, for, while, etc.).

> O Python diferencia maiúsculas de minúsculas, então nome e Nome são
> variáveis diferentes.

> Recomenda-se usar nomes descritivos para as variáveis, que indiquem
> claramente seu propósito: nome, idade, total_vendas, etc.

# Operadores

### Aritméticos

Os operadores aritméticos são utilizados para realizar operações matemáticas básicas. Os principais operadores aritméticos em Python são:

- Soma (+): soma dois valores.
- Subtração (-): subtrai o segundo valor do primeiro.
- Multiplicação (\*): multiplica dois valores.
- Divisão (/): divide o primeiro valor pelo segundo e devolve um resultado de tipo flutuante.
- Divisão inteira (//): divide o primeiro valor pelo segundo e devolve um resultado de tipo inteiro (a parte decimal é descartada).
- Módulo (%): devolve o resto da divisão entre o primeiro valor e o segundo.
- Exponenciação (\*\*): eleva o primeiro valor à potência do segundo.

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

- Igual a (==): devolve True se ambos os valores são iguais.
- Diferente de (!=): devolve True se os valores são diferentes.
- Maior que (>): devolve True se o primeiro valor é maior que o segundo.
- Menor que (<): devolve True se o primeiro valor é menor que o segundo.
- Maior ou igual que (>=): devolve True se o primeiro valor é maior ou igual que o segundo.
- Menor ou igual que (<=): devolve True se o primeiro valor é menor ou igual que o segundo.

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

- AND (and): devolve True se ambas as condições são verdadeiras.
- OR (or): devolve True se ao menos uma das condições é verdadeira.
- NOT (not): inverte o valor de uma condição, devolve True se a condição é falsa e False se a condição é verdadeira.

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

- **IF**

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

- **IF-ELSE**

A estrutura if-else nos permite especificar um bloco de código alternativo que será executado se a condição do if for falsa. A sintaxe básica é a seguinte:

```python
idade = 15


if idade >= 18:
   print ("Você é maior de idade.")

else:
   print ("Você é menor de idade.")
```

Neste exemplo, se a variável idade for maior ou igual a 18, será executado o bloco de código dentro do if e será impressa a mensagem "Você é maior de idade." Caso contrário, será executado o bloco de código dentro do else e será impressa a mensagem "Você é menor de idade."

- **IF-ELIF-ELSE**

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

- **Break**

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

- **Continue**

A instrução continue é utilizada para pular o restante do bloco de código dentro de um loop e passar para a próxima iteração.

Exemplo:

```python
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)
```

Neste exemplo, o loop for itera sobre os números de 0 a 9 utilizando a função range(). Dentro do loop, verifica-se se o número é divisível por 2 utilizando o operador de módulo %. Se o número for divisível por 2 (ou seja, se for par), a instrução continue é executada, fazendo com que o restante do bloco de código seja pulado e passando para a próxima iteração do loop. Como resultado, apenas os números ímpares serão impressos.

- **Pass**

A instrução pass é uma operação nula que não faz nada. É utilizada como um marcador de posição quando uma instrução é sintaticamente necessária, mas nenhuma ação é desejada.

Exemplo:

```python
for i in range(5):
    pass
```

Neste exemplo, o loop for itera sobre os números de 0 a 4, mas nenhuma ação é realizada dentro do loop devido à instrução pass. Isso pode ser útil quando se está desenvolvendo um programa e se deseja reservar um bloco de código para implementá-lo mais tarde.

# Estruturas de dados

### Listas

Uma lista é uma estrutura de dados mutável e ordenada que permite armazenar uma coleção de elementos. Os elementos de uma lista podem ser de diferentes tipos de dados e são encerrados entre colchetes [], separados por vírgulas.

- **Criação e acesso**

Para criar uma lista, simplesmente encerre os elementos entre colchetes:

```python
frutas = ["maçã", "banana", "laranja"]
```

Para acessar os elementos de uma lista, utilize o índice do elemento entre colchetes. Os índices começam a partir de 0.

```python
print(frutas[0])  # Imprime "maçã"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "laranja"
```

Você também pode acessar os elementos a partir do final da lista utilizando índices negativos. O índice -1 representa o último elemento, -2 representa o penúltimo, e assim por diante.

```python
print(frutas[-1])  # Imprime "laranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "maçã"
```

- **Métodos de listas**

As listas em Python têm vários métodos incorporados que nos permitem manipular e modificar os elementos da lista. Alguns métodos comuns são:

- **append(elemento):** adiciona um elemento ao final da lista.
- **insert(indice, elemento):** insere um elemento em uma posição específica da lista.
- **remove(elemento):** remove a primeira ocorrência de um elemento na lista.
- **pop(indice):** remove e retorna o elemento em uma posição específica da lista.
- **sort():** ordena os elementos da lista em ordem ascendente.
- **reverse():** inverte a ordem dos elementos na lista.

Exemplo:

```python
frutas = ["maçã", "banana", "laranja"]


frutas.append("pera")
print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]


frutas.insert(1, "uva")
print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]


frutas.remove("banana")
print(frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]


fruta_removida = frutas.pop(2)
print(frutas)  # Imprime ["maçã", "uva", "pera"]
print(fruta_removida)  # Imprime "laranja"


frutas.sort()
print(frutas)  # Imprime ["maçã", "pera", "uva"]


frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "maçã"]
```

- **Listas de compreensão**

As listas de compreensão são uma forma concisa de criar novas listas baseadas em uma sequência existente. Permitem filtrar e transformar os elementos de uma lista em uma única linha de código.

```python
nova_lista = [expressão for elemento in sequência if condição]
```

Exemplo:

```python
números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados)  # Imprime [4, 16]
```

Neste exemplo, é criada uma nova lista chamada quadrados, que contém os quadrados dos números pares da lista números. A expressão x \*\* 2 eleva cada elemento ao quadrado, e a condição if x % 2 == 0 filtra apenas os números pares.

### Tuplas

Uma tupla é uma estrutura de dados imutável e ordenada que permite armazenar uma coleção de elementos. Os elementos de uma tupla são encerrados entre parênteses (), separados por vírgulas.

- **Criação e acesso**

Para criar uma tupla, encerre os elementos entre parênteses:

```python
ponto = (3, 4)
```

Para acessar os elementos de uma tupla, utilize o índice do elemento entre colchetes, similar às listas:

```python
print(ponto[0])  # Imprime 3

print(ponto[1])  # Imprime 4
```

Ao contrário das listas, as tuplas são imutáveis, o que significa que não podem ser modificadas uma vez criadas. Não se pode adicionar, eliminar ou alterar elementos em uma tupla existente.  
As tuplas são úteis quando você precisa armazenar uma coleção de elementos que não devem ser modificados, como coordenadas ou dados de configuração.

- **Métodos de Tuplas**

Embora as tuplas sejam imutáveis, Python fornece vários métodos úteis para trabalhar com elas:

- **count(elemento):** devolve o número de vezes que um elemento aparece na tupla.
- **index(elemento):** devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca.
- **len(tupla):** embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.

```python
minha_tupla = (1, 2, 3, 2, 4, 2)


print (minha_tupla.index(2))   # Saída: 1

print (minha_tupla.index(2, 2))   #Saída: 3

print (minha_tupla.index(2, 2, 4))   #Saída: 3
```

### Dicionários

Um dicionário é uma estrutura de dados mutável e não ordenada que permite armazenar pares de chave-valor. Cada elemento em um dicionário consiste em uma chave única e seu valor correspondente. Os dicionários são delimitados por chaves {}, e os pares chave-valor são separados por vírgulas.

- **Criação e acesso**

Para criar um dicionário, utilize chaves e separe as chaves e valores com dois pontos.

`pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}`

Para acessar os valores de um dicionário, utilize a chave correspondente entre colchetes:

```python
print(pessoa["nome"])  # Imprime "João"
print(pessoa["idade"])    # Imprime 25
print(pessoa["cidade"])  # Imprime "Madri"
```

Você também pode utilizar o método get() para obter o valor de uma chave. Se a chave não existir, retorna um valor padrão (por padrão, None).

- **Métodos de dicionários**

Os dicionários em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:

- **keys():** retorna uma visualização de todas as chaves do dicionário.
- **values():** retorna uma visualização de todos os valores do dicionário.
- **items():** retorna uma visualização de todos os pares chave-valor do dicionário.
- **update(outro_dicionario):** atualiza o dicionário com os pares chave-valor de outro dicionário.

Exemplo:

```python
pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}


print(pessoa.keys())    # Imprime dict_keys(["nome", "idade", "cidade"])
print(pessoa.values())  # Imprime dict_values(["João", 25, "Madri"])
print(pessoa.items())   # Imprime dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])


pessoa.update({"profissao": "Engenheiro"})
print(pessoa)  # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}
```

### Conjuntos (set)

Um conjunto é uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos. Os conjuntos são delimitados por chaves {} ou são criados utilizando a função set().

- **Criação e operações básicas**

Para criar um conjunto, utilize chaves ou a função set():

```python
frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])
```

Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}


intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}


diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}


diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}
```

- **Métodos de conjuntos**

Os conjuntos em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:

- **add(elemento):** adiciona um elemento ao conjunto.
- **remove(elemento):** remove um elemento do conjunto. Se o elemento não existir, gera um erro.
- **discard(elemento):** remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
- **clear():** remove todos os elementos do conjunto.

Exemplo:

```python
frutas = {"maçã", "banana", "laranja"}


frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()
```

As estruturas de dados em Python nos oferecem grande flexibilidade e potência para armazenar e manipular dados em nossos programas. As listas são úteis para coleções ordenadas e mutáveis, as tuplas para coleções ordenadas e imutáveis, os dicionários para armazenar pares de chave valor e os conjuntos para coleções não ordenadas de elementos únicos.

# Funções

As funções são blocos de código reutilizáveis que nos permitem encapsular tarefas específicas e executá-las quando necessário. As funções nos ajudam a organizar nosso código, evitar a repetição e fazer com que nossos programas sejam mais modulares e fáceis de manter.

### Definição e Chamada de Funções

Para definir uma função em Python, utilizamos a palavra-chave **def** seguida do nome da função e parênteses. Opcionalmente, podemos especificar parâmetros dentro dos parênteses. O bloco de código da função é indentado após os dois pontos.

Para chamar uma função, simplesmente escrevemos o nome da função seguido de parênteses:

```python
def saudacao():
    print("Olá, mundo!")

saudacao()  # Imprime "Olá, mundo!"
```

### Parâmetros e Argumentos

As funções podem aceitar parâmetros, que são valores que são passados para a função quando ela é chamada. Os parâmetros são especificados dentro dos parênteses na definição da função.

```python
def saudacao(nome):
    print(f"Olá, {nome}!")
```

Ao chamar a função, fornecemos os argumentos correspondentes aos parâmetros:

```python
saudacao("João")  # Imprime "Olá, João!"
saudacao("Maria")  # Imprime "Olá, Maria!"
```

### Valores de Retorno

As funções podem retornar valores usando a palavra-chave return. O valor de retorno pode ser usado pelo código que chama a função

```python
def soma(a, b):
    return a + b


resultado = soma(3, 4)
print(resultado)  # Imprime 7
```

### Funções Anônimas (lambda)

Python permite criar funções anônimas ou funções lambda, que são funções sem nome definidas em uma única linha. São comumente usadas para funções pequenas e concisas.

```python
quadrado = lambda x: x ** 2
print(quadrado(5))  # Imprime 25
```

### Escopo das Variáveis (local x global)

As variáveis definidas dentro de uma função têm um escopo local, o que significa que só são acessíveis dentro da função. Por outro lado, as variáveis definidas fora de qualquer função têm um escopo global e podem ser acessadas de qualquer parte do programa.

```python
def funcao():
    variavel_local = 10
    print(variavel_local)  # Acessível dentro da função


variavel_global = 20


def funcao2():
    print(variavel_global)  # Acessível de qualquer lugar


funcao()  # Imprime 10
funcao2()  # Imprime 20
print(variavel_global)  # Imprime 20
print(variavel_local)  # Gera um erro, a variável não está definida neste escopo.
```

### Funções definidas pelo usuário

- **Documentação de funções (docstrings)**

É uma boa prática documentar nossas funções utilizando docstrings. Os docstrings são cadeias de texto que descrevem o propósito, os parâmetros e o valor de retorno de uma função. São colocados imediatamente após a definição da função e são encerrados entre aspas duplas triplas.

```python
def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.


    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.


    Returns:
        float: A área do retângulo.
    """
    return base * altura
```

- **Funções com número variável de argumentos**

  Python permite definir funções que aceitem um número variável de argumentos. Isso é feito utilizando o operador \* antes do nome do parâmetro.

```python
   def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(soma_variavel(1, 2, 3))  # Imprime 6
print(soma_variavel(4, 5, 6, 7))  # Imprime 22
```

As funções são uma ferramenta fundamental na programação e nos permitem estruturar e modularizar nosso código. Com a capacidade de definir funções personalizadas, podemos encapsular tarefas específicas e reutilizá-las em diferentes partes do nosso programa.

Além das funções definidas pelo usuário, Python também fornece uma ampla gama de funções incorporadas que podemos utilizar diretamente, como print(), len(), range(), entre outras.

# Tratamento de Erros e Exceções

Quando escrevemos programas, é comum nos depararmos com situações inesperadas ou erros durante a execução. Python fornece um mecanismo para lidar com esses erros de maneira controlada utilizando o tratamento de exceções. Isso nos permite capturar e lidar com erros específicos sem que o programa pare abruptamente.

### Erros comuns em Python

Antes de mergulharmos no tratamento de exceções, vejamos alguns erros comuns que você pode encontrar em Python

- **Erro de sintaxe (SyntaxError)**

Ocorre quando o código não segue as regras de sintaxe do Python, como esquecer dois pontos após uma declaração de função ou um loop.

```python
def minha_funcao() # Faltam os dois pontos
    print("Olá")
```

- **Erro de nome (NameError)**

Ocorre quando se faz referência a uma variável ou função que não foi definida.

```python
print(variavel_nao_definida)
```

- **Erro de tipo (TypeError)**

Ocorre quando se realiza uma operação com tipos de dados incompatíveis, como tentar somar um número e uma string.

```python
resultado = 5 + "10"
```

- **Erro de índice (IndexError)**

Ocorre quando se tenta acessar um índice fora do intervalo válido de uma lista ou sequência.

```python
lista = [1, 2, 3]
print(lista[3])  # O índice 3 está fora do intervalo
```

Estes são apenas alguns exemplos de erros comuns. Quando ocorre um erro, Python gera uma exceção e exibe uma mensagem de erro que inclui o tipo de exceção e uma descrição do problema.

### Manejo de Exceções

O manejo de exceções nos permite capturar e lidar com erros de maneira controlada utilizando as declarações try, except e opcionalmente finally.

- **Try**

O bloco try contém o código que pode gerar uma exceção. Se ocorrer uma exceção dentro do bloco try, o fluxo de execução é transferido para o bloco except correspondente.

```python
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
```

- **Except**

O bloco except especifica o tipo de exceção que se deseja capturar e lidar. Você pode ter múltiplos blocos except para lidar com diferentes tipos de exceções.

```python
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")
```

- **Finally**

O bloco finally é opcional e é executado sempre, independentemente de ter ocorrido uma exceção ou não. É comumente utilizado para realizar tarefas de limpeza ou liberação de recursos.

```python
try:
    # Código que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção
```

### Exceções Personalizadas

Além das exceções incorporadas no Python, você também pode criar suas próprias exceções personalizadas. Isso é útil quando deseja lidar com situações específicas do seu programa.

Para criar uma exceção personalizada, você deve criar uma classe que herde da classe base Exception ou de uma de suas subclasses.

```python
def funcao():
    # Código que pode gerar uma exceção personalizada
    if condicao:
        raise Exception("Descrição do erro")


try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")
```

Neste exemplo, define-se uma função chamada funcao(). Dentro da função, verifica-se uma condição e, se for satisfeita, gera-se uma exceção utilizando a declaração raise. Em vez de criar uma classe personalizada, utiliza-se diretamente a classe base Exception para gerar a exceção.

Depois, utiliza-se um bloco try-except para capturar e lidar com a exceção. A variável e é utilizada para acessar a descrição do erro fornecida ao gerar a exceção.

O tratamento de erros e exceções é uma parte fundamental da programação em Python. Permite lidar com situações inesperadas de maneira controlada e evitar que seu programa trave ou pare abruptamente.

Quando ocorre um erro no seu código, o Python gera uma exceção. Ao utilizar blocos try-except, você pode capturar e lidar com essas exceções de maneira adequada. Pode especificar diferentes blocos except para lidar com diferentes tipos de exceções e realizar ações específicas em cada caso.

Além disso, o bloco finally permite executar código de limpeza ou liberação de recursos, independentemente de ter ocorrido uma exceção ou não. Isso é útil para garantir que certas ações sejam sempre realizadas, como fechar arquivos ou conexões de banco de dados.

**Importante!**

Considere os possíveis erros que podem ocorrer no seu código e utilize o tratamento de exceções adequado para lidar com eles de maneira apropriada. Isso tornará seus programas mais robustos e confiáveis.
