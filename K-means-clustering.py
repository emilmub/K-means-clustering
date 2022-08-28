import numpy as np

def distancia(a,b):
	'''
	Mide la distancia euclidiana entre dos vectores

	Argumentos:
		a: primer vector
		b: segundo vector

	Returns:
		dist: distancia entre a y b
	'''
	dist = 0
	for i in range(len(a)):
		dist += (a[i]-b[i])**2
		print(dist)

	dist = np.sqrt(dist)

	return dist

def promedio(datos):
	'''
	Calcula el valor promedio de los datos acomodados como columnas cada vector diferente

	Argumentos:
		datos: matriz con los datos a promediar

	Returns:
		prom: vector con el promedio de los datos
	'''

	prom = np.zeros([len(datos),1])
	for i in range(datos.shape[0]):
		suma = 0
		for j in range(datos.shape[1]):
			suma += datos[i,j]
			print(suma)
		prom[i,0] = suma/datos.shape[0]
	return prom

datos = np.array([[1,4,7],[2,5,8],[3,6,9]])
print(promedio(datos))