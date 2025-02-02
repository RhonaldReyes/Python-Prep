#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:
lista1 = []
i = -15
while i < 0:
    lista1.append(i)
    i += 1
print(lista1)




# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:
#Si sería posible y para desmotrarlo, usaremos la lista anterior.
lista1 = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
i = -15
while (i < 0):
    if i % 2 == 0: 
        print(i)
    i += 1




# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:
lista1 = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
for i in lista1:
    if i % 2 ==  0:
        print(i)




# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:
lista1 = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
for i in lista1[0:3]:
    print(i)



# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:
lista1 = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

print(list(enumerate(lista1)))



# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:
lista1 = [1,2,5,7,8,10,13,14,15,17,20]
i = 1
while i <= 20:
    if not i in lista1:
        lista1.insert(i-1,i)
    i+=1
print(lista1)




# In[11]:






# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:
fibo=[0, 1]
i = 2
while i < 30:
    fibo.append(fibo[i-2] + fibo[i-1])
    i += 1
print(fibo)





# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:
print(sum(fibo))



# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:
#Este ejercicio no lo entendí ni mirando la respuesta, así que copié y pegué.

ultimos = 30  
n = ultimos - 5  

while n < ultimos:  
    print(fibo[n] / fibo[n - 1])  
    n += 1  



# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:
cadena = "Hola mundo. Esto es una practica del lenguaje de programación Python"
posiciones = []
for i, c in enumerate(cadena):
    if c == "n":
        posiciones.append(i)
    
print(posiciones)




# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:
dicc1 = {
    "Ciudad": ["Bueos Aires", "Caracas", "Bogota", "Quito", "Montevideo"], 
    "País": ["Argentia", "Venezuela", "Colombia", "Ecuador", "Uruguay"],
    "Continente": ["America", "America", "America", "America", "America"],
} 
for i in dicc1:
    print(i) 




# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:
cadena = list(cadena)
for i in cadena:
    print(i)






# In[45]:
#usando la función iter()
cadena = list(cadena)
iterador = iter(cadena)
rango = len(cadena)
if i in range(0, rango):
    print(next(iterador))




# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 0]
combi = zip(lista1, lista2)
print(tuple(combi))




# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:
lis = [18, 21, 29, 32, 35, 42, 56, 60, 63, 71, 84, 90, 91, 100]
divisible_entre_siete = [i for i in lis if i % 7 == 0]
print(divisible_entre_siete)




# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
i = 0 
for c in lis:
    if type(c) == list:
        i += len(c)
    else:
        i += 1

print(i)



# In[51]:





# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
lis_convertidos = []
for i in lis:
    if type(i) != list:
        i = [i]
    lis_convertidos.append(i)

print(lis_convertidos)


