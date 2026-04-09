# ler um número inteiro e dizer se ele é par ou ímpar.
while True:
    # Ler um número inteiro
    numero = int(input("Digite um número inteiro: "))

    # Verificar se é par ou ímpar
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

    # Perguntar se deseja continuar
    resposta = input("Deseja continuar (sim/não)? ").strip().lower()

    if resposta == "não" or resposta == "nao":
        print("Programa encerrado.")
        break