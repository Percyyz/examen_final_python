"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

list_numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
num_primos = list(filter(es_primo, list_numeros))
print(num_primos)