"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me ´permita editar uno de los campos del registro
"""

alumno = {
   1:{"nombre": "Percy",
    "apellido": "Yarihuaman",
    "edad": 20,
    "programa": "APSTI",
    "unidad didactica":"Lenguaje de programacion",
    "semestre":"III"
},
    2:{
    "nombre": "Willam",
    "apellido": "Barrientos",
    "edad": 18,
    "programa": "APSTI",
    "unidad didactica":"Lenguaje de programacion",
    "semestre":"III"
    }
}
def imprimir_registros(alumno):
    for id_registro,datos in alumno.items():
        print(id_registro,datos)
imprimir_registros(alumno)