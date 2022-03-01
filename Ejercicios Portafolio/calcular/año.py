# Un año es bisiesto si es divisible por 4 y no es por 100, 
# o si es divisible por 400. Escribe un programa que lea un año 
# y devuelva si es bisiesto o no.

año = int(input('Introduce año: '))

if año % 4 == 0 and año % 100!=0 or año %400==0:
    print(año," es un año bisiesto")
else:
    print(año," no es un año bisiesto")