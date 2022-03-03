#Ejemplo continue en Python #1

num_1 = 0

for num_1 in range(5):
    if num_1 == 2:
        continue

    print('El número es:', num_1)
print('Finalizando Programa')

#imprimirá
#El número es: 0
#El número es: 1
#El número es: 3
#El número es: 4
#El número es: 5
#Finalizando Programa