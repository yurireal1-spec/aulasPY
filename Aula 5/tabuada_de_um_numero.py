import os, time
#Gerando números com for 
Valor=int(input("Digite um Valor: "))

print(f"Tabuada do {Valor}")
for i in range(1,11):
    print(f"{Valor} x {i} = {Valor*i}")

time.sleep(6)
os.system("cls")