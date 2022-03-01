# Calcular de la suma y la media aritmetica de N numeros reales. Solicitar el valor de N al usuario
#  y cada uno de los N numeros reales
n = 2  
suma = 0
med_arit = 0

for i in range(2):
    num = int(input('Ingrese valor ' + ': '))
    suma = suma + num
print('El resultado de la suma es: ', suma)

med_arit += suma/2

print('La med aritmetica es: ', med_arit)
