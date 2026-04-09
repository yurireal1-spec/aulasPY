filmes = []
a = ""
i = 1
while a!= 'fim': 
    a = input(f"informe o {i}º filme: ")
    i+=1
    if a!= "fim":
        filmes.append(a)
        #print(filmes)
    else: 
        print(filmes)
        