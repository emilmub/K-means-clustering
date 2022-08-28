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
		prom[i,0] = suma/datos.shape[0]

	return prom

def clasif_centros(datos,dimensiones,centros,K):
	'''
	Clasifica cada punto en datos dependiendo del centro que se encuentre mas cerca

	Argumentos:
		datos: conjunto de puntos en la base de datos
		dimensiones: dimensiones de la base de datos
		centros: conjunto de puntos denominados "centroides"
		K: numero de puntos "centroide"

	Returns:
		ind_centros: clasificacion con cada centroide
	'''

	ind_centros = np.zeros([dimensiones[0],1])

	for i in range(dimensiones[0]):
		min_dist = np.inf
		ind_min = 0
		for j in range(K):
			dist = distancia(datos[i],centros[j])
			if min_dist > dist:
				min_dist = dist
				ind_max = j
		ind_centros[i] = ind_max

	return ind_centros

def K_means_clustering(datos,K,aleatorio = True,centros = None):
	'''
	Algoritmo para clasificar un conjunto de puntos en el espacio

	Argumentos:
		datos: conjunto de puntos en el espacio, arreglo de numpy
		K: numero de centroides, entero
		aleatorio: True si los centroides seran puntos aleatorios del conjunto, False si se introduciran manualmente, booleano
		centros: centroides iniciales si aleatorio == False, arreglo de numpy
	
	Returns:

	'''

	dimensiones = datos.shape

	if aleatorio:
		indices = np.random.choice(dimensiones[0],size = K,replace = False) # Escoge K puntos aleatorios de datos
		indices = np.sort(indices)
		centros = np.zeros([K,dimensiones[1]])
		j = 0
		for i in indices:
			centros[j] = datos[i]
			j += 1
	elif centros is None:
		raise Exception("Es necesario introducir los centros si se desactiva la opcion aleatoria")
	elif centros.shape[0] != K:
		raise Exception('Es necesario que el numero de puntos coincida con K')
	elif centros.shape[1] != dimensiones[1]:
		raise Exception('Es necesario que los centros tengan las mismas dimensiones que los puntos dados')

	ind_centros = clasif_centros(datos,dimensiones,centros,K)
	print(ind_centros)

if __name__ == '__main__':
	datos = np.array([[1,2,3],[4,5,6],[7,8,9]])
	cent = np.array([[0,0,0],[1,1,1]])
	K_means_clustering(datos,3)