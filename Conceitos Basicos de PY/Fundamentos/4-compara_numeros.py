while True:
    # Ler dois números inteiros
    n1 = int(input("Digite o primeiro número: ")) #usuario escolhe o primeiro número, que será atribuido ao "n1"
    n2 = int(input("Digite o segundo número: "))#usuario escolhe o segundo número, que será atribuido ao "n2"

    # Verificar qual é maior ou se são iguais
    if n1 > n2: #confirma se o ni é maior que n2, caso sim mostrar o resultado.
        print(f"{n1} é o maior")
    elif n2 > n1: #confirmar se o n2 é maior que n1, caso sim mostrar o resultado.
        print(f"{n2} é o maior")
    else: #se ambos forem iguais apresentar o resultado do else.
        print("Os números são iguais")

    # Perguntar se deseja continuar
    if input("Deseja continuar? (sim/não) ").strip().lower() != "sim": #após resultado loop criado com a pergunta de deseja continuar.
        print("Programa encerrado.")
        break
'''
.strip() e .lower() tem a função de ajustar o espaços e letras Maiusculas na aplicação.

O != "sim"
Se a resposta for diferente de 'sim', então execute o bloco abaixo." E se o usuario digitar sim vai ser reconhecido e o while faz o loop novamente.
'''