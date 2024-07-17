"""
Crear una funcion que me me retorne un diccionario con los datos personales de un alumno
ejm:
entrada: ("jose","alvarez","30","APSTI","III")
salida: {nombre:"jose",apellido:"alvarez",edad:"30",programa_estudio:"APSTI",semestre:"III"}
"""

def datos_alumno(nombre,apellido, edad, programa_estudio, semestre):
    datos_alumno ={
        "nombre": nombre,
        "apellido":apellido,
        "edad": edad,
        "programa_estudio": programa_estudio,
        "semestre": semestre
    }
    return datos_alumno
datos = datos_alumno("percy","yarihuaman", 20, "APSTI", "III")
print(datos)