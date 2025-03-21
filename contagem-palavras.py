""" CONTAGEM DE PALAVRAS
* Crie uma função que recebe uma string e conta quantas vezes cada palavra aparece nela.
Retorne um dicionário onde a chave é a palavra e o valor é a quantidade de ocorrências.
"""

frutas = ["Pêra Uva Maçã Pêra Pêra Maçã Uva"]

def contar_ocorrencias(frutas):
    lista_de_frutas = frutas[0].split()
    
    contador = {}
    
    for fruta in lista_de_frutas:
        if fruta in contador:
            contador[fruta] += 1
        else:
            contador[fruta] = 1
            
    return contador

resultado = contar_ocorrencias(frutas)

print(f'Quantas vezes aparece cada fruta? {(resultado)}')