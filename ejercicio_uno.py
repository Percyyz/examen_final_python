"""
crear un funcion que reciba como parametro una lista de numeros y me retorne dos valores el numero menor y el numero mayor en un diccionario
ejem:
entrada: [4,7,10,4,1,0]
salida : {menor:0,mayor:10}
"""

def min_max(l):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n

    maximo=l[0]
    for n in l:
        if n > maximo:
            maximo=n
    return {"minimo":minimo, "maximo":maximo}
lista_numeros=[1,3,54,6,5,3]
resultado=min_max(lista_numeros)
print (resultado)
