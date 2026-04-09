import os
#Testando sequencia lógica e atribuições variaveis.
'''
Este  código lê dois números do tipo float
Respresentando a base e altura e calcula a área do triângulo.
'''
resposta="sim"
while resposta=="sim":
    #Entrada
    os.system('cls')
    base = float (input("Digite o valor da base: "))
    altura = float (input("Informe o valor da altura: "))
    #Processamento
    area = base * altura / 2
    #Saida
    print (f"A área do triangulo é {area}")
    resposta=input("\nDeseja continuar (sim/não)? ")
