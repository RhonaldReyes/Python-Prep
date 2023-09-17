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
num3 = 5
if type(num3) == int and num3 > 0:
    num4 = num3
    while (num3 > 1):   
        num3 = num3 -1
        num4 = num4 * num3
    print(f"El facorial es {num4}")




# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
#Para este ejercicio me he planteado como reto hacer un ciclo que sume todos los numeros pares hasta 10
num5 = 0
while (num5 < 11):
    for num6 in range(1,11):
        if num6 % 2 == 0:
            num5 = num5 + num6
    print("La suma de todos los pares del 1 al 10 es", num5)




# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
n = 5
for i in range(1, n):
    while(n < 5):
        n -= 1
    print('Ciclo while nro ' + str(n))
    print('Ciclo for nro ' + str(i))




# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
n = 0
while (n < 30):
    esPrimo = True
    for i in range (2, n):
        if (n % i == 0):
            esPrimo = False
    if (esPrimo == True):
        print(n)
    n += 1


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
n = 0
while (n < 30):
    esPrimo = True
    for i in range (2, n):
        if (n % i == 0):
            esPrimo = False
            break
    if (esPrimo == True):
        print(n)
    n += 1



# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
#este no lo etendí así que solo copié y pegué.
ciclos_sin_break = 0
n = 0
primo = True
while (n < 30):
    for div in range(2, n):
        ciclos_sin_break += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))



# In[57]:
ciclos_con_break = 0
n = 0
primo = True
while (n < 30):
    for div in range(2, n):
        ciclos_con_break += 1
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')



# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:
n = 99
while (n <= 300):
    n += 1
    if (n % 12 != 0):
        continue
    print(n)




# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
while (n <= 300):
    if(n % 6 == 0):
        print(n)
        break
    n += 1    



# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:
while (n <= 300):
    if(n % 6 == 0):
        print(n)
        break
    n += 1    


