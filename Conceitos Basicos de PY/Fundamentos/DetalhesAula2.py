"""
============================================================
DOCUMENTAÇÃO EXPLICATIVA – AULA 2 PYTHON
Autor: Diogo Silva
Descrição: Aplicação demonstrando manipulação de strings,
concatenação, tipagem e conversão de dados.
============================================================

1. OBJETIVO DO PROGRAMA
------------------------------------------------------------
Esta aplicação tem como objetivo aprofundar os conceitos
iniciais da linguagem Python, explorando:

- Manipulação de strings
- Atribuição de variáveis
- Concatenação de dados
- Conversão de tipos (type casting)
- Uso de f-strings
- Entrada de dados pelo usuário
- Tratamento de erro de tipo (TypeError)

O programa também foi executado no modo interativo (REPL),
permitindo testar operações diretamente no console.


2. SAÍDA DE DADOS – FUNÇÃO print()
------------------------------------------------------------
A função print() é responsável por exibir informações
na tela. Tecnicamente, ela envia dados para a saída padrão
do sistema (stdout).

Exemplo:
print("Boa noite!")

O texto entre aspas é uma STRING.
String é um tipo de dado usado para representar textos.


3. VARIÁVEIS E ATRIBUIÇÃO
------------------------------------------------------------
Exemplo:
nome = "Fernando"
sobrenome = "Prestes"

Aqui temos a criação de variáveis.

O símbolo "=" é chamado de operador de atribuição.
Ele associa um valor a uma variável.

Em Python:
- Variáveis armazenam referências a objetos na memória.
- A linguagem utiliza tipagem dinâmica, ou seja,
  o tipo do dado é definido automaticamente.

Tipos utilizados nesta aula:
- str (string)
- int (inteiro)


4. F-STRING (STRING FORMATADA)
------------------------------------------------------------
Exemplo:
print(f"Escola Técnica {nome} {sobrenome}")

A letra "f" antes das aspas indica uma f-string
(formatted string literal).

Ela permite inserir variáveis dentro do texto
utilizando chaves {}.

Durante a execução:
- O Python avalia as variáveis
- Converte para string se necessário
- Monta a frase final

Essa forma é mais moderna e recomendada
para construção de textos dinâmicos.


5. CONCATENAÇÃO DE STRINGS
------------------------------------------------------------
Concatenação é o processo de unir duas ou mais strings.

Exemplo:
texto1 + " " + texto2

O operador "+" quando aplicado a strings
realiza a junção dos textos.

Importante:
Para que a concatenação funcione,
os dois lados da operação devem ser do mesmo tipo.


6. ERRO DE TIPO (TypeError)
------------------------------------------------------------
Durante a execução foi gerado o erro:

TypeError: can only concatenate str (not "int") to str

Esse erro ocorre porque o Python é fortemente tipado.
Ele não permite operações entre tipos diferentes
sem conversão explícita.

Exemplo incorreto:
"texto" + 10

Não é permitido somar string com inteiro.


7. CONVERSÃO DE TIPO (TYPE CASTING)
------------------------------------------------------------
Para corrigir o erro, foi utilizada a função:

str(a)

Isso converte o valor inteiro para string.

Esse processo é chamado de conversão explícita
de tipo (type casting).

Exemplo correto:
escola + str(a)

Agora ambos são do tipo string,
permitindo a concatenação.


8. CONVERSÃO IMPLÍCITA NA F-STRING
------------------------------------------------------------
Exemplo:
f"{escola} Nota: {a}"

Na f-string, o Python converte automaticamente
o inteiro para string.

Essa conversão ocorre de forma implícita,
utilizando o método interno de formatação.


9. ENTRADA DE DADOS – FUNÇÃO input()
------------------------------------------------------------
Exemplo:
escola = input("Onde você estudou anteriormente? ")

A função input():
- Exibe uma mensagem
- Aguarda o usuário digitar
- Retorna o valor digitado como string

Importante:
O retorno do input() é sempre do tipo string.

Neste caso, ocorreu também uma reatribuição:
A variável "escola" recebeu um novo valor,
substituindo o anterior.


10. EXECUÇÃO NO MODO INTERATIVO (REPL)
------------------------------------------------------------
Os testes foram realizados no console Python,
identificado pelo símbolo >>>.

O console funciona no modelo REPL:
- Read (Ler)
- Evaluate (Avaliar)
- Print (Exibir)
- Loop (Repetir)

Isso permite testar comandos individualmente
e visualizar resultados imediatamente.


11. CONCEITOS IMPORTANTES APRENDIDOS
------------------------------------------------------------
Nesta aula foram aplicados os seguintes conceitos:

✔ Manipulação de strings
✔ Concatenação com operador +
✔ Tipagem dinâmica
✔ Sistema de tipos (str e int)
✔ Conversão explícita de tipo (str())
✔ Conversão implícita via f-string
✔ Tratamento de erro TypeError
✔ Reatribuição de variável
✔ Execução interativa (REPL)


12. CONCLUSÃO
------------------------------------------------------------
A Aula 2 aprofundou o entendimento sobre:

- Como Python trata diferentes tipos de dados
- Como funciona a concatenação
- Por que ocorre erro ao misturar tipos
- Como realizar conversão de forma correta
- Diferença entre concatenação manual e f-string

Esse conhecimento é essencial para evitar erros comuns
ao trabalhar com entrada de dados, cálculos e geração
de textos dinâmicos.

A compreensão da tipagem e da conversão de dados
é um passo fundamental para evolução em programação.

============================================================
FIM DA DOCUMENTAÇÃO
============================================================
"""