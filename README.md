# Qué es Python?
Python es un lenguaje de programación interpretado,sencillo de leer y escribir debido a su alta similitud con el lenguaje humano. Además, se trata de un lenguaje multiplataforma de código abierto y, por lo tanto, gratuito, lo que permite desarrollar software sin límites.
# Qué es una variable?
Dependiendo del lenguaje de programacion una variable puede indicar al programa de qué lugar empieza a existir, qué nombre tendrá y qué tipo de datos almacenarás, es un elemento que se emplea para almacenar y hacer referencia a otro valor o para explicarlo de una manera mas sencilla, es una caja el cual seria la variable  en la cual puede estar almacenado un valor o bien agregarle uno.
## Nombrando una variable
La creación de variables se realiza a través de la asignación de un valor a la misma. El operador de asignación en Python es el “=“

Correcta asignacion de variable
```python
x=10
```
Incorrecta asignacion de variable
```python
10=x
```
## Asignando valores a una variable
Los valores o datos es lo que nuestra variable anteriormente creada almacenará dentro, para esto debemos tener pensado si nuestra variable almacenará un valor numérico o un valor.

Asignando un valor numérico a nuestra variable:
```python
valor numerico=20
```
En este caso  el valor colocado no llevo comilla ya que asi pythom lo reconocera automaticamente como un valor numerico, pero si este mismo se le agregara comillas pythom lo reconoceria como un texto,por ejemplo:
```python
nombre_animal:'perro'
```
## Operadores básicos

### Suma
El operador de la suma  funciona como una suma normal, se suma los numeros usados por el programa o usuario a travez de pythom por ejemplo:
```python
resultado = 10 + 5
print(resultado)
```
Se creo una variable que dentro contenga una operacion, en el cual seria la suma de los numeros, despues se escribio print y se coloca el nombre de la variable que seria "resultado", y al final se imprimira en pantalla el  resultado de la operacion.

### Resta
Es igal a la suma solo que en vez de sumar los numeros asignados se los restan,por ejemplo:
```python
resultado= 30 - 15
print(resultado)
```
Ocurrio lo que paso con el operador de la suma,solo que aqui se realizo lo correspondido que seria la resta del 30 - 15, dando su resultado para luego imprimir en pantalla.

### Multiplicación
Este operador lógico en programación se lo representa de la siguiente forma: * , ya que es el símbolo que usa el intérprete de python para referirnos que la operación que se llevará a cabo será una multiplicación,por ejemplo:
```python
resultado = 4 * 3
print(resultado)
```
En este caso el programa multiplicara el 4 con el 3 para luego guardar el resultado en la variable "resultado", dando como respuesta 12 para luego imprimir en pantalla la respuesta.

### División
Para python se usara el  slash /, el cual indica que la operación que se llevará a continuación es una división, por ejemplo:
```python
resultado = 15 / 3
print(resultado)
```
Aqui se llevo a cabo la division entre el numero 15 y el 3 el cual obtenido el resultado, se escribe el print para imprimir en pantalla.
### Módulo
El operador módulo da como resultado el resto de la división entera, el simbolo para este operador es el %, por ejemplo:
```python
num1=6
num2=20
modulo=num1%num2
print(num1,'%',num2,'=',modulo)
```
Como se dijo el modulo da como resultado el resto de la division entera, aqui esta un ejemplo de como modular con dos variables
# Tipos de datos en Python
Los tipos de datos son:
```
*Numeros enteros
*Numeros de punto flotante
*Texto(cadena de caracteres)
*Booleanos(Verdaderos y falso)
```

## Integer
Este tipo de de datos se corresponde con números enteros, es decir numeros que no tengan decimales, aqui se usa el comando "int" para representarlo,por ejemplo:
```python
a = int(2)
print(a)
```
## Float
Este tipo de dato corresponde a los numeros reales con partes decimales. En python el que separa los decimales es el  punto "." y no la coma ",". Aqui se usa el comando "float" para representarlo,por ejemplo:
```python
resultado = 5.2 + 2.5
print(resultado)
print(type(resultado))  #Se imprimirá <class 'float'>
```
En este  ejemplo, el programa luego de imprimir el resultado , debajo de este imprimirá el tipo de dato que és en el siguiente formato: <class 'float'>, que da a entender que el tipo de dato resultante es float.

## String
Este tipo de datos corresponde con una cadena de caracteres que representa un texto,se usa el comando "str" para representarlo con comillas simples o dobles, por ejemplo:

Usando comillas dobles:
```python
comida_favorita = "Hamburguesas" 
print(comida_favorita)             
```
Usando comillas simples:
```python
comida_favorita = 'Hamburguesas'
print(comida_favorita)             
```
## Casting en Python
El casting es la tecnica que sirve para convertir un dato de un tipo a un tipo de dato diferente,por ejemplo:
```python
int a str: str(25)
str a int: int ("89")
float a int: int (5.3)
```
## List
Son conjuntos ordenados de elementos, los valores de diferentes tipos de datos básicos se pueden agrupar y los elementos se pueden agregar, eliminar o cambiar de las listas en cualquier momento es decir mutables, se representan con corchetes"[]", comillas "" y comas ",".Por ejemplo:
```python 
list = [9,6,5["nueve",seis","cinco"]]
print(list)
```
## Tuple
Las tuplas en python es un conjunto ordenado de elementos que se encuentran encerrados por paréntesis y separados por comas, casi como si fuera una lista, que una tupla no puede ser una tupla vacía(no tener ningún elemento dentro), y tampoco puede cambiar el orden ni datos dentro de ellas, por ejemplo:
```python
tuple=[carro,casa,televisor]
print:("tuple")
```   
## Dictionary
Dictionary es un tipo de dato en python,que nos permiten almacenar cualquier tipo de valor como enteros, cadenas, listas e incluso otras funciones.Un dato que debemos tener muy en cuenta a la hora de crearlo  es que debemos almacenar nuestros datos en {} o llaves, por ejemplo:
```python
diccionario = {'Nombre': 'John', 'Edad': 19}
print(diccionario)
```
# Tomando decisiones
Las decisiones en pythom son muy importantes en el momento de decidir si nuestro program ejecute una orden, pero para esto se tiene que cumplir con algunas condiciones anteriores, para conseguir esto en python se usa la sentencia if
## Sentencia if
Es una forma común de controlar el flujo de un programa, lo que te permite ejecutar bloques de código específicos según el valor de algunos datos. Si la condición que sigue a la palabra clave if se evalúa como verdadera, el bloque de código se ejecutará.
#Escribir un programa que solicite un valor entero al usuario
#determine si es par o impar
```python
num=int(input("ingrese numero:"))

if (num%4==0):
    print("El numero es par",)
    print(num,"es par")
else:
    print("El numero es impar")
```
## Ciclo For
EN python el ciclo for es una estructua que repite una serie de instrucciones por un numero determinado de veces(bucle)estos bucles, como su nombre indica, nos permiten ejecutar una o más líneas de código de forma iterativa, por ejemplo:
```python
print("Comienzo")
for _ in [0, 1, 2]:
    print("Hola ", end="")
print()
print("Final")
```                                     
## Ciclo While
El ciclo while valúa una condición y luego ejecuta un bloque de código solo si la condición dada por el programa es verdadera, el código seguirá ejecutandose hasa que la condición sea falsa, por ejemplo:
```python
#10-20

num=11

while num<10 or num >20 or num%2!=0:
    num=int(input("ingrese numero:"))

print("se fue")
```
## Break

## Continue
