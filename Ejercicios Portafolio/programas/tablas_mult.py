#Calcular e imprimir la tabla de multiplicar de un numero cualquiera
#Imprimir el multiplicando, el multiplicador y el producto.
Num = int(input('ingrese el número: '))

for m in range(1,13):
	multi = m * 2 
	print(f'{Num} x {m} = {multi}') 