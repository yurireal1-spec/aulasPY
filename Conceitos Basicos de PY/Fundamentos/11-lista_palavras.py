palavra = []
p = ""
i = 1
while p!= 'fim': 
    p = input(f"informe a {i}ª palavra: ")
    if p!= "fim":
        palavra.append(p)
    i+=1
print(palavra)
for i, p in enumerate(palavra,start=1):
    print(f"{i}ª = {p}")

palavra.sort()

print(palavra)
