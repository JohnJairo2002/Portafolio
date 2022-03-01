# Calcular el mayor de 4 numeros enteros introducidos por el teclado

num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
num3 = int(input("Ingrese tercer numero: "))
num4 = int(input("Ingrese cuarto numero: "))

if num1 < num2:
    num1, num2 = num2, num1

if num1 < num3:
    num1, num3 = num3, num1

if num2 < num3:
    num2, num3 = num3, num2

print('Mayor: ', num1)
print('Medio: ', num2)
print('Menor: ', num3)


