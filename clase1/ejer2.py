'''
Evaluación de estudiantes: 
Dado un array de estudiantes (nombre, notas[]), calcula el promedio individual y 
muestra los que aprobaron (promedio ≥ 11) y su mención (suficiente, bueno, excelente). 
'''
estudiantes=[{"nombre":"Pepe","notas":[12,15,15,17]},{"nombre":"Santi","notas":[20,13,12,11]},{"nombre":"David","notas":[10,12,15,13]}]
mencion=""

for estudiante in estudiantes:
    promedio= sum(estudiante["notas"])/len(estudiante["notas"])
    if promedio>=11:
        if promedio>=17:
            mencion="Excelente"
        elif promedio>= 14:
            mencion="Bueno"
        else:
            mencion="Suficiente"
        print(estudiante["nombre"], promedio, mencion)
    else:
        print("Desaprobado")










'''
DICCIONARIOS

notas= {"Santi":[19,12,14,16,20]}
español={"celular":"Dispositivo que sirve para comunicarte", "amor":"Sentimiento hacia algo o alguien"}
print(español["celular"])
print(español["amor"])
print(notas["Santi"])
print(notas)
'''