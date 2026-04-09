"""
============================================================
DOCUMENTAÇÃO EXPLICATIVA – AULA 2.1 PYTHON
Autor: Diogo Silva
Descrição: Aplicação para cálculo da área de um triângulo,
demonstrando entrada, processamento e saída de dados.
============================================================

1. OBJETIVO DO PROGRAMA
------------------------------------------------------------
Este programa tem como objetivo calcular a área de um triângulo
utilizando a fórmula matemática:

    área = (base * altura) / 2

Além do cálculo em si, a aplicação demonstra conceitos
fundamentais da programação em Python, como:

- Entrada de dados pelo usuário
- Conversão de tipos
- Operações matemáticas
- Atribuição de variáveis
- Uso de f-strings
- Modelo Entrada → Processamento → Saída (IPO)


2. DOCSTRING (DOCUMENTAÇÃO INICIAL)
------------------------------------------------------------
O bloco delimitado por três aspas duplas (\"\"\")
é chamado de docstring.

Ele serve para documentar o programa.
Diferente do comentário com #, a docstring pode ser
acessada internamente pelo Python através do atributo __doc__.

Ela é utilizada para descrever o propósito da aplicação.


3. ENTRADA DE DADOS – FUNÇÃO input()
------------------------------------------------------------
Exemplo:

base = float(input("Digite o valor da base: "))

A função input() realiza:

1. Exibição de uma mensagem ao usuário.
2. Espera pela digitação de um valor.
3. Retorno do valor digitado como STRING.

Tecnicamente:
- input() lê dados da entrada padrão (stdin).
- O retorno é sempre do tipo str.


4. CONVERSÃO DE TIPO – float()
------------------------------------------------------------
Como input() retorna uma string, é necessário converter
o valor para um tipo numérico antes de realizar cálculos.

A função float() realiza a conversão explícita de tipo
(type casting), transformando o texto digitado em um
número de ponto flutuante.

Tipo float:
- Representa números reais.
- Utiliza representação de ponto flutuante (IEEE 754).

Exemplo:
"10" → 10.0
"5.5" → 5.5

Se a conversão não for possível (ex: texto inválido),
o programa gera um erro chamado ValueError.


5. ATRIBUIÇÃO DE VARIÁVEIS
------------------------------------------------------------
Exemplo:

base = float(...)
altura = float(...)

O operador "=" é chamado de operador de atribuição.

Ele associa o valor retornado pela função à variável.

Em Python:
- Variáveis armazenam referências a objetos na memória.
- A linguagem utiliza tipagem dinâmica, ou seja,
  o tipo é definido automaticamente em tempo de execução.


6. PROCESSAMENTO – CÁLCULO MATEMÁTICO
------------------------------------------------------------
Exemplo:

area = base * altura / 2

Essa etapa representa o processamento do programa.

Operadores utilizados:
- *  → multiplicação
- /  → divisão

O Python segue regras de precedência matemática:

1. Multiplicação
2. Divisão
3. Avaliação da esquerda para a direita

Tecnicamente, o interpretador:
- Busca o valor de base
- Busca o valor de altura
- Realiza a multiplicação
- Divide o resultado por 2
- Armazena o valor final na variável area

Esse processo é chamado de avaliação de expressão
aritmética em tempo de execução.


7. MODELO IPO (ENTRADA → PROCESSAMENTO → SAÍDA)
------------------------------------------------------------
O programa segue o modelo clássico da computação:

ENTRADA:
    input()

PROCESSAMENTO:
    area = base * altura / 2

SAÍDA:
    print(...)

Esse modelo é conhecido como IPO
(Input → Process → Output).

Ele representa a estrutura básica de sistemas computacionais.


8. SAÍDA DE DADOS – FUNÇÃO print()
------------------------------------------------------------
Exemplo:

print(f"A área do triangulo é {area}")

A função print() envia dados para a saída padrão (stdout),
normalmente o terminal.

Foi utilizada uma f-string (formatted string literal),
indicada pela letra "f" antes das aspas.

As f-strings permitem inserir variáveis dentro do texto
usando chaves {}.

O valor numérico (float) é convertido automaticamente
para string durante a formatação.


9. TIPOS DE DADOS UTILIZADOS
------------------------------------------------------------
Durante a execução do programa foram utilizados:

- str   → para mensagens de texto
- float → para números reais
- variáveis → referências para objetos na memória

A linguagem Python utiliza tipagem dinâmica e forte,
ou seja:
- O tipo é definido automaticamente.
- Não permite operações inválidas entre tipos diferentes.


10. POSSÍVEL ERRO
------------------------------------------------------------
Se o usuário digitar um valor não numérico,
como por exemplo:

"abc"

A função float() não conseguirá converter o valor
e será gerado um erro chamado:

ValueError

Esse comportamento demonstra a importância
da validação de dados e do tratamento de exceções,
assunto abordado em níveis mais avançados.


11. CLASSIFICAÇÃO DO PROGRAMA
------------------------------------------------------------
Este programa pode ser classificado como:

- Programa sequencial
- Programa determinístico
- Aplicação matemática básica
- Implementação de fórmula geométrica

Ele utiliza apenas estrutura sequencial,
não possuindo decisões (if) nem repetições (laços).


12. CONCLUSÃO
------------------------------------------------------------
A Aula 2.1 representa a transição do trabalho com
strings para o uso de dados numéricos e cálculos.

Foram consolidados conceitos fundamentais como:

✔ Entrada de dados
✔ Conversão de tipos
✔ Operações matemáticas
✔ Modelo IPO
✔ F-strings
✔ Tipagem dinâmica
✔ Processamento aritmético

Esse conhecimento é essencial para evoluir
para estruturas condicionais, laços de repetição
e programas mais complexos.

============================================================
FIM DA DOCUMENTAÇÃO
============================================================
"""