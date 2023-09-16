#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
num1 = 5
print(num1)



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
print(type(8.5))




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
print(type(num1))




# 4) Crear una variable que contenga tu nombre

# In[2]:
name = "Rhonald"



# 5) Crear una variable que contenga un número complejo

# In[3]:
num2 = 7 + 5j




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(num2))




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
import numpy as np
print(round(np.pi, 4))




# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
elvi = "True"
elvi1 = True
#no son el mismo tipo de variable




# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print(type(elvi))
print(type(elvi1))




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
num3 = 5 + 5.5
print(num3)




# 11) Realizar una operación de suma de números complejos

# In[2]:
num4 = 3 + 3j
num5 = 6 -2j
print(num4+num5)




# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
print(num1+num5)




# 13) Realizar una operación de multiplicación

# In[5]:
print(num1*3)




# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
print(2**8)



# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
num6 = 27
num7 = 4
print(num6/num7)




# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
print(27//4)




# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
print(27%4)




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
print(4*6 +3)




# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
lastname = " Reyes"
print(name + lastname)




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
print(2 == "2")
#Ocurre porque uno es un sting y el otro un entero.




# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
print(2 == int("2"))




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

#Ocurre porque al utilizar la coma, en lugar del punto, lo reconoce como una cadena 
# de texto y no puede transformarlo en float. Si se usa el punto, si lo transforma.




# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
num8 = 3
num8 -= 1
print(num8)




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
1 << 2
#El sistema de numeración binario es un sistema representado solo por 1 y 0. 
#Este resultado se da, porque el viario de 1 es 000000001 (sin imprtar el número de ceros a la izquierda),
#al pedirle que se desplace el 1 dos espacios nos queda 0000100, que es el equivalente a 4




# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
#2 + "2"
#La operación nos arroja error porque uno es una string y el otro un int. No es posible sumarlos ni concatenarlos
#No, no daría lo mismo. Haciendo 2 + 2 realizaría una suma de int arrojando 4 como resultado.
#mientras que hacendo "2" + "2", concatenaría ambas string dando 22 como resultado.





# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
a = "Ja"
b = "Si fue gracioso"
print(a*5 + " " + b)


