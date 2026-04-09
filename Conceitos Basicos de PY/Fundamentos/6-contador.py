#i = 1 #Variavel i é int
nome = input("Qual seu nome: ")
print(f"Olá {nome}.")
valor_inicial = int(input("Valor inicial: "))
i = valor_inicial
valor_final = int(input("Valor final: "))

while i <= valor_final:
    if i < valor_final:
        # Ainda não é o último, então usa vírgula
        print(f"{i}, ",end="")
    else:
    # É o último valor, então usa ponto final
        print(f"{i}.")
    i+=1