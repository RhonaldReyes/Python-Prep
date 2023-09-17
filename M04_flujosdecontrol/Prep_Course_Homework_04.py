#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
num1 = 7
if num1 > 0:
    print("El número es mayor que 0")
elif num1 < 0:
    print("El número es menor que 0")
else:
    print("Número no válido.")




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
name = "Rhonald"
age = 33
if type(name) == type(age):
    print("Son del mismo tipo")
else:
    print("No son del mismo tipo")




# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
for x in range(1, 21):
    if x%2 == 0:
        print(f"El número {x} es par")
    else:
        print(f"El número {x} es impar")




# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for i in range(6):
    print(f"La tercera potencia de {i} es igual a {i**3}")




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
num2 = 9
for a in range(num2):
    print(f"{a+1} Estoy en rango")




# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:





# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:





# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:





# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:




# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:





# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:




# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:





# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:




# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:



