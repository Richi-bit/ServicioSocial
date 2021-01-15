import random
import numpy as np
import math

#Coordenadas de referencia iniciales
xi = 3
yi = 3
zi = 3

save = [] #Matriz que guardará las coordenadas de cada átomo
i = 1

ejemplo = open("Ejemplo.txt", "w") #Archivo txt donde se guardarán las coordenadas
atomo = input("Atomo ") #Acción para teclear el elemento
numAtoms = input("Numero de atomos ") #Acción para teclear la cantidad de átomos
minDist = input("Distancia interatomica minima ")
maxDist = input("Distancia interatomica maxima ")
ejemplo.write(str(atomo) + "\n") #Escribe el texto del átomo y da un salto de línea
ejemplo.write("\n") #Salto de linea
while i <= int(numAtoms): #El 5 es solo un ejemplo de la cantidad de átomos que se van a colocar
	#Guardado de variables
	xn = xi
	yn = yi
	zn = zi
	#Números aleatorios de las coordenadas
	xi = random.uniform(-xi, xi)*10
	yi = random.uniform(-yi, yi)*10
	zi = random.uniform(-zi, zi)*10
	#Matriz donde se guardan las coordenadas
	matriz = [xi, yi, zi]
	if math.sqrt((xn - xi)**2 + (yn - yi)**2 + (zn - zi)**2) >= float(maxDist) or math.sqrt((xn-xi)**2 + (yn - yi)**2 + (zn - zi)**2) <= float(minDist):
		#Condiciones de distancias interatómicas. Si se cumplen, entonces las variables xi, yi y zi deberán tomar el valor de la iteración anterior.
		xi = xn
		yi = yn
		zi = zn
		#Si se cumple la condición, i no avanza hasta que deje de cumplirse la condición y pase al else.
	else:
		#Si la condición no se cumple: save.append() me agrega las 3 coordenadas a la matriz save
		save.append(matriz)
		print(save[i - 1]) #Esto solo escribe en consola lo que se va guardando en la matriz save
		#Se guardan las coordenadas xyz de la última matriz. Se inicia desde 0 y termina en 2.
		x = matriz[0]
		y = matriz[1]
		z = matriz[2]
		#Me agrega cada fila de la matriz en el archivo txt del inicio
		ejemplo.write(str(atomo) + "	" + str(x) + "	" +	str(y) + "	" + str(z) + "\n")
		i = i + 1 #Siguiente iteración