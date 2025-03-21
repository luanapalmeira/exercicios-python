""" ORDENAÇÃO DE TUPLAS 
* Dada uma lista de tuplas, onde cada tupla contém o nome de uma pessoa e sua idade,
escreva uma função que retorne a lista ordenada pela idade de forma crescente.
"""

amigos = [('Lucas', '21'), ('Rodrigo', '31'), ('Angela', '24'), ('Marcela', '19'), ('Raissa', '15')]

amigos_ordem_crescente = sorted(amigos, key=lambda amigo: amigo[1])

print(f'Colocando em ordem crescente ficaria: {amigos_ordem_crescente}')