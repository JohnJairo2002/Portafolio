#Ejemplo continue en Python #3

num_1 = 0

for num_1 in range(8):
    if num_1 == 4:
        continue

    print('El número es:', num_1)
print('Finalizando Programa')

#imprimirá
#El número es: 0
#El número es: 1
#El número es: 2
#El número es: 3
#El número es: 5
#El número es: 6
#El número es: 7
#El número es: 8
#Finalizando Programa