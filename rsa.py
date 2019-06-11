## p y q primos
## n = pq
##p, q, a privados
##n y b publicas
# --- ek(x) = x ^b mod n   para encriptar
# --- dk(y) = y ^a mod n   para desencriptar

from exponenciacion import *
from generadorPrimos import *
from inversoModular import *
from primalidad import *
from random import *

def gcd(a, b):
	if( b == 0):
		return a
	else:
		return gcd(b, a % b)

#GENERACION DE CLAVES#

print("Generacion de claves: ")
#p = generarPrimo(20)
#q = generarPrimo(20)

p = 409
q = 503

n = p * q

print("n publica: {}".format(n))

fiDeN = (p - 1)*(q - 1)

print("Q(n): {}".format(fiDeN))

digitosFiDeN = len(str(fiDeN))
esCoprimo = False
b = 0

while not esCoprimo:
	
	b = generarPrimo(digitosFiDeN - 1)
	
	if gcd(b, fiDeN) == 1:
		esCoprimo = True

b = 101
print("publicas: ")
print("b: {}".format(b))

a = inversoModular(b, fiDeN)

print("Privadas: \n")
print("a {}".format(a))
print("p: {}\nq: {}".format(p, q))


msj = int(input("Ingrese un numero: "))
encrypt = exponenciacionModulo(msj, b, n)

print("Mensaje encriptado: {}".format(encrypt))

desencrypt = exponenciacionModulo(encrypt, a, n)

print("Mensaje desencriptado: {}".format(desencrypt))

#firma ?:
#cifrado:   F = h^a(R)  mod n
#des: h = F^b(R) mod n
############