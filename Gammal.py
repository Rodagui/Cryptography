from exponenciacion import*
from generadorPrimos import*
from inversoModular import*
from primalidad import*
from random import *


# Python Program to find the factors of a number

def obtenerFactoresPrimos(n): 
	factores = set({})

	if n % 2 == 0:
		factores.add(2)

	while n % 2 == 0: 
		n = n // 2

	raiz = int(n ** 0.5)
	
	for i in range(3, raiz + 1, 2): 
		  
		# while i divides n , print i ad divide n 
		while n % i== 0: 
			factores.add(i)
			n = n // i 

	if n > 2:
		factores.add(n)

	return list(factores)

# change this value for a different result.
num = 320

# uncomment the following line to take input from the user
#num = int(input("Enter a number: "))





#para calcular el elemento generador o primitivo: #

p = generarPrimo(5)
q = generarPrimo(5)

#p = 53
#q = 71

numPrimo = False
i = 1

while not numPrimo:
	i +=1

	if( esPrimo(i*p*q + 1)):
		numPrimo = True

pAsterisco = i*p*q + 1
factoresPrimos = obtenerFactoresPrimos(pAsterisco - 1)
print("{}, {}".format(i, pAsterisco))
print("Factores primos de p*-1: {}".format(factoresPrimos))


alfa = 1
esGenerador = False

while not esGenerador:
	alfa += 1
	esGenerador = True

	for i in range(len(factoresPrimos)):
		primo = factoresPrimos[i]

		if exponenciacionModulo(alfa, (pAsterisco - 1) // primo, pAsterisco) == 1:
			esGenerador = False
			break

print("alfa (generador): {}".format(alfa))

k = randint(1, pAsterisco - 1)
#k= 1203
#a llave privada
a = generarPrimo(3)
# x es el mensaje
# = 1399
x = int(input("Mensaje: "))
beta = exponenciacionModulo(alfa, a , pAsterisco)


#se manda y1 y y2
y1 = exponenciacionModulo(alfa, k, pAsterisco)
y2 = multiplicacionExponenteModulo(x, 1, beta, k, pAsterisco)

print("y1: {}\ny2: {}".format(y1, y2))

#desencriptar

inv = inversoModular(y1**a, pAsterisco)

#forma "lenta"
desncrypted = multiplicacionModulo( y2, inv, pAsterisco)
print("Resultado 1: {}".format(desncrypted))


#froma chida
descifrado = multiplicacionExponenteModulo(y1, pAsterisco - a - 1, y2, 1, pAsterisco)
print("Resultado 2: {}".format(descifrado))