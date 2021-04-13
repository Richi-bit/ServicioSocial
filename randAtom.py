import random
import numpy as np
import math

xi = random.uniform(-3,3)
yi = random.uniform(-3,3)
zi = random.uniform(-3,3)

save = []
i = 1
k = 1

ejemplo = open(str(k) + ".txt", "w")
atomo = input("Atomo ")
numAtoms = input("Numero de atomos ")
cluster = input("Numero de clusters ")
minDist = input("Distancia interatomica minima ")
maxDist = input("Distancia interatomica maxima ")
ejemplo.write(str(atomo) + "\n")
ejemplo.write("\n")
while i <= int(numAtoms):
	xn = xi
	yn = yi
	zn = zi
	xi = random.uniform(-xi, xi)*10
	yi = random.uniform(-yi, yi)*10
	zi = random.uniform(-zi, zi)*10
	matriz = [xi, yi, zi]
	if math.sqrt((xn - xi)**2 + (yn - yi)**2 + (zn - zi)**2) >= float(maxDist) or math.sqrt((xn-xi)**2 + (yn - yi)**2 + (zn - zi)**2) <= float(minDist):
		xi = xn
		yi = yn
		zi = zn
	else:
		save.append(matriz)
		print(save[i - 1])
		x = matriz[0]
		y = matriz[1]
		z = matriz[2]
		ejemplo.write(str(atomo) + "	" + str(x) + "	" +	str(y) + "	" + str(z) + "\n")
		i = i + 1

deform = np.array(save)
step = 0.8

for i in range(int(cluster) - 1):
	ejemplo2 = open(str(i + 2) + ".txt", "w")
	ejemplo2.write(str(atomo) + "\n")
	ejemplo2.write("\n")
	for j in range(len(deform)):
		deform[j] = deform[j] + (random.uniform(-1,1) * step)
		print(deform[j])
		finMat = []
		finMat.append(deform[j])
		xyz = finMat[0].tolist()
		ejemplo2.write(str(atomo) + "	" + str(xyz[0]) + "	" + str(xyz[1])+ "	" + str(xyz[2]) + "\n")