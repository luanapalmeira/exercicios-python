""" SOMA DE ELEMENTOS PARES 
* Escreva uma função que recebe uma lista de números inteiros e retorna a soma de todos os
elementos pares contidos nela.
"""

lista = [1, 2, 4, 5, 7, 8, 12, 15, 18]

def somar_numeros_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma

resultado = somar_numeros_pares(lista)

print(f'O resultado da soma dos números pares é: {resultado}')