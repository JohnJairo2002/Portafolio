#Suponga que se tiene un conjunto de calificaciones de un grupo de 40 alumnos. 
# Realizar un algoritmo para calcular la calificación media y la calificación más 
# baja de todo el grupo.

import sys

n = 5
suma = 0
menor = sys.maxsize

for i in range(n):
    num = int(input('Ingrese numero: '))
    suma += num
    if num<menor:
        menor = num

print("Promedio:", suma/n)
print("Menor:", menor)