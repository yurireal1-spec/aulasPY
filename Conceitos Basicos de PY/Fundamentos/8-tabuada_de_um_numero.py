import os
resposta="sim"
while resposta=="sim" or resposta=="s":
    os.system('cls')
    v1 = int(input("Quer a tabuada de quem? "))
    for i in range(1,11):
        print(f"{v1} x {i} = {v1*i}")
    resposta=input("\nDeseja continuar (sim/não)? ")
    if resposta == "não" or resposta == "nao":
        print("Programa encerrado.")
        break