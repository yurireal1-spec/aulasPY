#Classifica fase da vida
'''
Este código lê e informa a fase da vida
"Bebê", quando a idade for menor ou igual a 2
"Criança", quando a idade for menor ou igual a 10
"Pré-adolescente", quando a idade for menor a 15
"Adolescente" menor que 18 
"Jovem" menor ou igual a 30
"Adulto" menor que 60
"Melhor idade" maior ou igual a 60
'''
while True:  # Loop infinito até o usuário decidir sair
    idade = float(input("Informe a sua idade: "))
    
    if idade < 2:
        print("Bebê")
    elif idade <= 10:
        print("Criança")
    elif idade <= 15:
        print("Pré-Adolescente")
    elif idade < 18:
        print("Adolescente")
    elif idade <= 30:
        print("Jovem")
    elif idade <= 60:
        print("Adulto")
    else:
        print("Melhor idade")
        print("Bem jovem você em rsrs")
    
    # Pergunta se o usuário quer continuar
    continuar = input("Deseja continuar? (sim/não): ").strip().lower()
    if continuar != 'sim':  # Sai do loop se não for 'sim'
        print("Programa finalizado!")
        break