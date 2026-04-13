ListaNumeros = []
a = 0
i = 1
while a!=-999: 
    a = int(input(f"informe o {i}ª numero em nossa lista: "))
    if a!= -999:
        ListaNumeros.append(a)
    i+=1    #print(ListaNumeros)
else: 
    soma=0
   
    listp=[n for n in ListaNumeros if n %2==0 ]
    listi=[n for n in ListaNumeros if n %2==1 ]
    

    for z in ListaNumeros:
        soma+= z

    
    Maior= max(ListaNumeros)
    Minimo=min(ListaNumeros)
    IND_MAIOR=ListaNumeros.index(Maior)
    IND_MENOR=ListaNumeros.index(Minimo)

    media=sum(ListaNumeros)/len(ListaNumeros)    
    

    
    print(ListaNumeros)
    print(len(ListaNumeros))
    print(f"Foram informados {len(listp)} números pares")
    print(f"Foram informados {len(listi)} números impares")
    print(f"A somatoria dos numeros é: {soma}.")
    print(f"O maior número foi o {Maior} na posição de Nº: {IND_MAIOR}")
    print(f"O menor número foi o {Minimo} na posição de Nº: {IND_MENOR}")
    print(f"A média aritimética entre eles foi: {media}")


    #resultado= sum(ListaNumeros)
    #print(resultado)