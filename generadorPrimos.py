#para generar numeros primos p y q

from random import *


def intentarCompuesto(a, d, n, s):
	if pow(a, d, n) == 1:
		return False

	for i in range(s):
		if pow(a, 2 ** i * d, n) == n-1:
			return False
	
	return True # n  is definitely composite

def esPrimo(n, _precision_for_huge_n=16):
	if n in _primosConocidos:
		return True
	
	if any((n % p) == 0 for p in _primosConocidos) or n in (0, 1):
		return False
	
	d, s = n - 1, 0
	
	while not d % 2:
		d, s = d >> 1, s + 1
	
	if n < 1373653: 
		return not any(intentarCompuesto(a, d, n, s) for a in (2, 3))
	
	if n < 25326001: 
		return not any(intentarCompuesto(a, d, n, s) for a in (2, 3, 5))
	
	if n < 118670087467: 
		if n == 3215031751: 
			return False
		return not any(intentarCompuesto(a, d, n, s) for a in (2, 3, 5, 7))
	
	if n < 2152302898747: 
		return not any(intentarCompuesto(a, d, n, s) for a in (2, 3, 5, 7, 11))
	
	if n < 3474749660383: 
		return not any(intentarCompuesto(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
	
	if n < 341550071728321: 
		return not any(intentarCompuesto(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
	
	# otherwise
	return not any(intentarCompuesto(a, d, n, s) for a in _primosConocidos[:_precision_for_huge_n])

_primosConocidos = [2, 3]
_primosConocidos += [x for x in range(5, 1000, 2) if esPrimo(x)]

def generarNumero(cantidadDigitos, ultimosDigitos):
	n = str(choice(ultimosDigitos))

	for i in range(1, cantidadDigitos):
		digito = str(randint(1, 9))
		n = digito + n

	return int(n)

def generarPrimo(cantidadDigitos):
	p = 0
	tengoPrimo = False

	while not tengoPrimo:
		p = generarNumero(cantidadDigitos, [1, 3, 7, 9])
		tengoPrimo = esPrimo(p)

	return p


if __name__ == '__main__':
	#numDigitos = int(input("Numero de digitos: "))
	numDigitos = 5
	print(generarPrimo(numDigitos))
	print(generarPrimo(numDigitos))

