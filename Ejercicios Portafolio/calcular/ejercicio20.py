# Programa que calcule y presente el signo de zodiaco a partir de la
# introduccion por teclado del dia y mes de nacimiento como numeros enteros

dia = int(input("ingrese dia: "))
numero_de_mes = int(input("ingrese mes de nacimiento: "))

    
if dia>=22 and numero_de_mes==12 or dia<=20 and numero_de_mes==1:
    print('Tu signo es Capricornio')

if dia>=21 and numero_de_mes==1 or dia<=19 and numero_de_mes==2:
    print('Tu signo es Acuario')

if dia>=20 and numero_de_mes==2 or dia<=20 and numero_de_mes==3:
    print('Tu signo es Piscis')

if dia>=21 and numero_de_mes==3 or dia<=19 and numero_de_mes==4:
    print('Tu signo es Aries')

if dia>=20 and numero_de_mes==4 or dia<=20 and numero_de_mes==5:
    print('Tu signo es Tauro')

if dia>=21 and numero_de_mes==5 or dia<=21 and numero_de_mes==6:
    print('Tu signo es Geminis')

if dia>=22 and numero_de_mes==6 or dia<=21 and numero_de_mes==7:
    print('Tu signo es Cancer')

if dia>=22 and numero_de_mes==7 or dia<=21 and numero_de_mes==8:
    print('Tu signo es Leo')

if dia>=22 and numero_de_mes==8 or dia<=22 and numero_de_mes==9:
    print('Tu signo es virgo')

if dia>=23 and numero_de_mes==9 or dia<=22 and numero_de_mes==10:
    print('Tu signo es libra')

if dia>=23 and numero_de_mes==10 or dia<=21 and numero_de_mes==11:
    print('Tu signo es escorpio')

if dia>=22 and numero_de_mes==11 or dia<=21 and numero_de_mes==12:
    print('Tu signo es sagitario')