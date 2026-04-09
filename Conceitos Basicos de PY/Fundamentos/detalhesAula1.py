"""
============================================================
DOCUMENTAÇÃO TÉCNICA – APLICAÇÃO PYTHON (AULA 1)
Autor: Diogo Silva
Descrição: Programa introdutório demonstrando conceitos
fundamentais da programação em Python.
============================================================

1. OBJETIVO DO PROGRAMA
------------------------------------------------------------
Este programa tem como finalidade demonstrar os conceitos
básicos da linguagem Python, incluindo:

- Saída de dados (print)
- Entrada de dados (input)
- Declaração e atribuição de variáveis
- Operadores aritméticos
- Estruturas condicionais
- Interpolação de strings (f-strings)
- Controle de fluxo
- Indentação significativa

Trata-se de um programa procedural e interativo,
baseado no paradigma da programação estruturada.


2. COMENTÁRIOS
------------------------------------------------------------
O símbolo "#" é utilizado para inserir comentários no código.
Comentários são ignorados pelo interpretador Python e servem
para documentação e organização do código-fonte.

Eles aumentam a legibilidade e facilitam manutenção futura.


3. SAÍDA DE DADOS – FUNÇÃO print()
------------------------------------------------------------
A função print() é uma função embutida (built-in function)
da linguagem Python.

Ela envia dados para a saída padrão (stdout),
geralmente o terminal.

Exemplo:
print("Boa noite")

Strings são delimitadas por aspas simples (' ') ou duplas (" ").


4. VARIÁVEIS E ATRIBUIÇÃO
------------------------------------------------------------
Exemplo:
b = 10
a = 5
r = a + b

O operador "=" é um operador de atribuição.
Ele associa um valor a um identificador (variável).

Em Python:
- Variáveis são referências para objetos na memória.
- O tipo é definido dinamicamente (tipagem dinâmica).

Tipos utilizados:
- int (inteiro)
- str (string)

A expressão:
r = a + b

Representa:
- Avaliação de expressão aritmética
- Operador de adição (+)
- Armazenamento do resultado em memória


5. IMPRESSÃO DE VARIÁVEIS
------------------------------------------------------------
Quando usamos:

print(a)

Estamos passando como argumento o valor armazenado na variável,
não um texto literal.

Diferença:
print("a")  → imprime a letra "a"
print(a)    → imprime o valor da variável a


6. ENTRADA DE DADOS – FUNÇÃO input()
------------------------------------------------------------
A função input() captura dados da entrada padrão (stdin).

Exemplo:
nome = input("Qual o seu nome? ")

Características técnicas:
- O programa pausa sua execução
- Aguarda interação do usuário
- Retorna sempre uma string
- O valor digitado é armazenado em variável

Isso caracteriza um programa interativo.


7. INTERPOLAÇÃO DE STRINGS – F-STRINGS
------------------------------------------------------------
Exemplo:
print(f"Boa noite {nome}, tudo bem?")

As f-strings (formatted string literals):
- Foram introduzidas no Python 3.6
- Permitem inserir variáveis dentro de strings
- Utilizam chaves {} para interpolação

São mais eficientes e legíveis que o método .format().


8. ESTRUTURA CONDICIONAL – CONTROLE DE FLUXO
------------------------------------------------------------
Exemplo:

if resposta == "sim":
    print("Vamos continuar então...")
elif resposta == "não":
    print("Até a próxima!")
else:
    print("Resposta inválida")

Estrutura condicional permite alterar o fluxo do programa
com base em avaliação lógica.

Componentes:

- if → executa se condição for verdadeira
- elif → condição alternativa
- else → executa se nenhuma condição anterior for satisfeita

Operador utilizado:
== → operador de comparação de igualdade

Importante:
=  → atribuição
== → comparação


9. EXPRESSÕES BOOLEANAS
------------------------------------------------------------
A expressão:

resposta == "sim"

Retorna um valor booleano:
- True  → executa o bloco
- False → ignora o bloco

Python utiliza o tipo bool para representar valores lógicos.


10. INDENTAÇÃO SIGNIFICATIVA
------------------------------------------------------------
Python utiliza indentação para definir blocos de código.

Diferente de linguagens como C, Java ou PHP,
que utilizam chaves {}, Python define blocos
através de espaçamento consistente.

A indentação faz parte da sintaxe da linguagem.


11. CLASSIFICAÇÃO DO PROGRAMA
------------------------------------------------------------
Este programa pode ser classificado como:

- Programa procedural
- Programa interativo
- Baseado em programação estruturada

Ele aplica os três pilares da programação estruturada:

1. Sequência
2. Decisão
3. (Repetição ainda não implementada)


12. CONCEITOS IMPLÍCITOS APLICADOS
------------------------------------------------------------
Mesmo sendo uma aplicação simples, foram utilizados
conceitos fundamentais da Ciência da Computação:

- Associação de identificadores a objetos
- Avaliação de expressões
- Manipulação de tipos primitivos
- Entrada e saída padrão (stdin / stdout)
- Controle de fluxo condicional
- Interação humano-computador
- Execução sequencial de instruções


13. CONSIDERAÇÕES FINAIS
------------------------------------------------------------
Esta aplicação representa a base do aprendizado em Python,
consolidando fundamentos essenciais para evolução futura,
como:

- Laços de repetição (for, while)
- Funções
- Estruturas de dados (listas, dicionários)
- Programação orientada a objetos
- Tratamento de exceções

Ela estabelece os princípios estruturais necessários
para desenvolvimento de aplicações mais complexas.

============================================================
FIM DA DOCUMENTAÇÃO
============================================================
"""