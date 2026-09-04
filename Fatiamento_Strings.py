Movie_Name = 'Exterminador do Futuro'
# string [incio:fim] indice comeca na posica 0 / indice final -1

# 1 -buscar toda string a partir da primeira posicao 
print(Movie_Name[0:]) # Exterminador do Futuro

# 2 - buscar toda string até a ultima posicao
print(Movie_Name [:21]) # Exterminador do Futuro

# 3 - buscar toda string da terceira posicao ate a ultima posicao
print(Movie_Name[2:]) # terminador do Futuro

"""
string [incio:fim:passo] 
indice comeca na posica 0 / indice final - 1
passo - determina o incremento do indice, ou seja, quantos indices pular,
por padrao esse numero é o 1.
"""

# 4 - buscar toda a string de dois em dois caractere
print(Movie_Name[::2])

# 5 - buscar toda a string nos indicies impares
print(Movie_Name[1::2])

# 6 - Inverter uma string de traz pra frente
print(Movie_Name[::-1])