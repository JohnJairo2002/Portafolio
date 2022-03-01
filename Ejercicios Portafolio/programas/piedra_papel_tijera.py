import random

#1 = piedra 
#2 = papel 
#3 = tijera

#while numero del 1 al 3
eleccion = int(input('Escoja: 1. piedra, 2. papel, 3. tijera: '))

num = random.randit(1,3)

if eleccion == num:
    print('Empate: ', eleccion, 'vs', num)
elif eleccion == 1:
    if num ==2:
        print('Pierdes: ', eleccion, 'vs', num)
    elif num == 3:
        print('Ganas: ', eleccion, 'vs', num)
elif eleccion == 2:
    if num ==1:
        print('Pierdes: ', eleccion, 'vs', num)
    elif num == 3:
        print('Ganas: ', eleccion, 'vs', num)
elif eleccion == 3:
    if num ==1:
        print('Pierdes: ', eleccion, 'vs', num)
    elif num == 2:
        print('Ganas: ', eleccion, 'vs', num)

# <1>jugar
#  elegir opcion
# <2> resultados
   #gane? perdi? empate?
# <0> Salir 