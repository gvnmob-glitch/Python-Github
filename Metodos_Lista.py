list_movies = ["Carros","Toy Story","Aliens","Rambo","Stallone Cobra","Robocop"]

# 1 - Descobrir o tamanho da lista e imprimir na tela.
print(len(list_movies))

# 2 - Recuperar um item da lista pelo seu nome.
print(list_movies.index("Rambo"))

# 3 - Adicionar um item ao final da lista.
list_movies.append("Spider-man")
print(list_movies)

# 4 - Ordenar a lista.
list_movies.sort()
print(list_movies)

# 5 - Copia os itens da lista para uma nova lista.
list_moviescopy = list_movies.copy()
list_moviescopy.remove('Toy Story')
print(list_moviescopy)

# 6 - Remove todos os itens da lista
list_movies.clear()
print(list_movies)
