# Determinar en que estado está el agua en función de su temperatura. 
# Si es negativa el estado será sólido, si es menor que 100 será líquido 
# y si es mayor que 100 será gas. Pedir al usuario el valor de la temperatura.

temp1 = int(input('Introduce la temperatura: '))
if temp1 <0:
    print("En ",temp1," grados Centigrados el agua está en estado sólido")
elif temp1 <100:
    print("En ",temp1," grados Centigrados el agua está en estado líquido")
else:
    print("En ",temp1," grados Centigrados el agua está en estado gaseoso")