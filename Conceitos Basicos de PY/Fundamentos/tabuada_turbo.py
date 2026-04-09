import os
resposta="sim"
while resposta=="sim" or resposta=="s":
    os.system('cls')
    n = int(input("Quer a tabuada de quem? "))
    print(f"Tabuada do n° {n}")
    print("="*15)
    for i in range(1,11):
                print(f"{n} x {i} = {n*i}")
    print("="*15)
    #aqui já estou fora do for
    resposta=input("\n\nDeseja ver mais tabuadas(sim/não)? ").strip().lower()
#aqui já estou fora do while