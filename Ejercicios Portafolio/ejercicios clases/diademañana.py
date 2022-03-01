# Solicitar al usuario una fecha (dd:mm:aaaa) y comprobar si es correcta
# El año debe ser mayor que cero
# El mes debe estar entre 1 y 12
# dependiendo del mes, el dia debe estar dentro de los limites validos

print('Se recibe una fecha en el formato dd:mm:aaaa y se indica si es correcta')
f=input("Introduce fecha (dd:mm:aaaa) ")
d=int(f[:2])
m=int(f[3:5])
a=int(f[6:])
if m<=0 or m>12 or d<=0 or d>31 or a<0:
    print("La fecha ",f," es incorrecta")
elif m in [1, 3, 5, 7, 8, 10, 12]: # Meses con 31 dias
    print("La fecha ",f," es correcta")
elif m in [4, 6, 9, 11] and d<=30: #Meses con 30 dias
    print("La fecha ",f," es correcta")
elif m==2 and d<=29: #Febrero en bisiesto tiene 29 dias, normal tiene 28
    if (a%4==0 and a%100!=0 or a%400==0):
        print("La fecha ",f," es correcta")
    elif d<=28:
        print("La fecha ",f," es correcta")
    else:
        print("La fecha ",f," es incorrecta")
else:
    print("La fecha ",f," es incorrecta")