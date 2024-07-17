"""
crear un funcion que me retorne un diccioonario de la cantidad de vocales que aparecen en un texto pasado por parametro el diccionario debera ser credo por comprension de diccionarios
ejm:
entrada: eucalipto
salida: {e:1,u:1,a:1,i:1,o:1}
"""
def contar_vocales(texto):
    vocales = 'aeiou'
    conteo_vocales = {vocal: 0 for vocal in vocales}
    for letra in texto:
        if letra in vocales:
            conteo_vocales[letra] += 1
    resultado = {vocal: conteo_vocales[vocal] for vocal in vocales if conteo_vocales[vocal] > 0}
    return resultado
texto = "eucalipto"
resultado = contar_vocales(texto)
print(resultado)