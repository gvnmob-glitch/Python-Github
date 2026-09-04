moviename = 'Batman Begins'
movie_description = 'Batman Begins is a 2005 superhero film directed by Christopher Nolan.'

print(moviename.upper()) # tudo maiusculo
print(moviename.lower()) # tudo minusculo 
print(moviename.title()) # primeira letra de cada palavra em maiusculo 
print(moviename.capitalize()) # primeira letra da primeira palavra em maiusculo e o restante em minusculo
print(moviename.center(30, '-')) # retorna a string cenralizada com caractere de preenchimento
print(moviename.find("g")) # retorna o indice do caractere procurado, caso nao encontre retorna -1
print(moviename.replace("Batman Begins", " The Dark Knight")) # substitui a palavra
print(movie_description.split(',')) # retorna uma lista com as palavras da string

