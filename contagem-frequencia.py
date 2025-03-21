""" CONTAGEM DE FREQUÊNCIA 
* Escreva uma função que recebe uma string e retorna um dicionário onde as chaves são os
caracteres da string e os valores representam quantas vezes cada caractere aparece.
"""

from collections import Counter

lista_de_esportes = ['Vôlei', 'Futebol', 'Basquete', 'Vôlei', 'Vôlei', 'Basquete', 'Futebol']

contagem = Counter(lista_de_esportes)

print(f'Quantas vezes aparece cada esporte? {(contagem)}')