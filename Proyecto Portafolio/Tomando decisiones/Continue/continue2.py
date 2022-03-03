#Ejemplo continue en Python #2

num_1 = 0

for num_1 in range(6):
    if num_1 == 3:
        continue

    print('El número es:', num_1)
print('Finalizando Programa')

#imprimirá
#El número es: 0
#El número es: 1
#El número es: 2
#El número es: 4
#El número es: 5
#El número es: 6
#Finalizando Programa