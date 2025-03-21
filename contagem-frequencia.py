""" CONTAGEM DE FREQUÊNCIA 
* Escreva uma função que recebe uma string e retorna um dicionário onde as chaves são os
caracteres da string e os valores representam quantas vezes cada caractere aparece.
"""

lista_de_esportes = ['Vôlei', 'Futebol', 'Basquete', 'Vôlei', 'Vôlei', 'Basquete', 'Futebol']

def contar_ocorrencias_esportes(lista_de_esportes):
    contagem = {}
    
    for esporte in lista_de_esportes:
        if esporte in contagem:
            contagem[esporte] += 1
        else:
            contagem[esporte] = 1
    return contagem

print(f'Quantas vezes aparece cada esporte? {contar_ocorrencias_esportes(lista_de_esportes)}')