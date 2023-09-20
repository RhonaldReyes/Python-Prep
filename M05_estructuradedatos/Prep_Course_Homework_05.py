#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:
lista1 = ["Bueos Aires", "Caracas", "Bogota", "Quito", "Montevideo"]



# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:
print(lista1[1])



# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:
print(lista1[1:4])




# 4) Visualizar el tipo de dato de la lista

# In[12]:
type(lista1)




# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:
print(lista1[2:])




# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:
print(lista1[:4])


    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:
#no arroja error:
lista1.append("Caracas")
lista1.append("Puerto Principe")
print(lista1)








# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:
lista1.insert(3, "Madrid")
print(lista1)




# In[21]:
lista1.insert(3, "Madrid")
print(lista1)


# 9) Concatenar otra lista a la ya creada

# In[22]:
lista1.extend(["Roma", "Lisboa", "Berlin"])
print(lista1)



# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:
lista1.index("Caracas")
#Si, se detiene al encontrarla la primera vez.




# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:
lista1.index("Cordoba")
#Manda error.




# 12) Eliminar un elemento de la lista

# In[25]:
lista1.remove("Lisboa")
print(lista1)




# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:
lista1.remove("Cordoba")




# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:
var1 = lista1.pop()
print(var1)




# 15) Mostrar la lista multiplicada por 4

# In[29]:
print(lista1*4)



# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:
tupla1 = (1, 2, 3, 4,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print(tupla1)



# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:
print(tupla1[10:15])



# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:
print(20 in tupla1)
print(30 in tupla1)




# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:
ciudad = "Paris"
if ciudad in lista1:
    print("La ciudad", ciudad, "esta en la lista")
else:
    lista1.append(ciudad)
    print("La ciudad", ciudad, "ha sido aregada.")




# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:
print(lista1.count("Caracas"))
print(tupla1.count("50"))




# 21) Convertir la tupla en una lista

# In[52]:
lista2 = list(tupla1)
print(type(lista2))




# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:
tupla2 = (1, 2, 3, 4,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
primero = [1]
segundo = [2]
tercero = [3]




# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:
dicc1 = {
    "Ciudad": lista1, 
    "País": ["Argentia", "Venezuela", "Colombia", "España", "Ecuador", "Uruguay", "Venezuela", "Haití", "Italia", "Segundo"],
    "Continente" : ["America", "America", "America", "Europa", "America", "America", "America", "America", "Europa", "Europa"]
}  
print(dicc1)





# 24) Imprimir las claves del diccionario

# In[59]:
print(dicc1.keys())



# 25) Imprimir las ciudades a través de su clave

# In[61]:
print(dicc1["Ciudad"])



