filmes =["Uma Batalha após a outra","MIB","Pecadores","Godzilla","Naruto"]

#1 - tamanho da lista
print(len(filmes))
#2 - recuperando o indice de um elemento pelo nome
print(filmes.index("Godzilla"))
#3 - Adicionar um item no final da lista
filmes.append("One Piece")
#4 - Ordena lista
filmes.sort()
print(filmes)
#5 - Copiar lista para outra
filmesCopia = filmes.copy()
print(filmesCopia)
#6 - inveertendo
filmesIntertido = sorted(filmes,reverse=True)
print(filmesIntertido)
#7 - Removendo
filmesIntertido.remove("MIB")
print(filmesIntertido)
#8 - Remover todos os itens da lista
filmesIntertido.clear()
print(filmesIntertido)
