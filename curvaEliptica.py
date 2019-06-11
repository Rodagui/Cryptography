#curvaEliptica
import random

def exponenciacionModulo(num, exponente, mod):
	res = 1
	num %= mod
	
	while exponente > 0:
		if exponente % 2 == 1:
			res = res * num % mod
		
		num = num * num % mod

		exponente = exponente // 2

	return res

def inversoModular(a, m) : 
	m0 = m 
	y = 0
	x = 1
  
	if (m == 1) : 
		return 0
  
	while (a > 1) : 
  
		q = a // m 
		t = m 
  
		m = a % m 
		a = t 
		t = y 
  
		y = x - q * y 
		x = t 
  
  
	if (x < 0) : 
		x = x + m0 
  
	return x

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


todas = False
q = 0

while(not todas):

	cumplen = False
	odd = False
	b = 0

	while(not cumplen):
		# 1. proponer un impar mayor que tres

		while(not odd):
			
			a = random.randint(5, 100)
			a = 651 
			
			if( a % 2 == 1):
				odd = True
			# 2. proponer un numero par mayor o igual a 2 (b)
		b = b + 2
		#print(b)

		b = 170

		# 3. checar las tres condiciones
		#si no se cumplen proponer otro b (paso 2)
		p = (a**2) + (b**2)
		if(esPrimo(p) and p % 4 == 1 and (a+b)%4 == 1):
			cumplen = True

	#4. calcular q
	q = (p+1+(2*a)) // 4

	#5. si q no es un num primo, propone un nuevo numero impar (paso 1)
	if(esPrimo(q)):
		todas = True



# 6. generar dos numeros aleatorios, menores que p - 1 y mayores que 1

todas = False
x1 = 0
y1 = 0
res1 = 0
res2 = 0

while(not todas):
	
	#xo y yo propuestos como solucion y son iguales a alfa (1)
	#xo = random.randint(2, p - 2)
	#yo = random.randint(2, p - 2)
	xo = 55211
	yo = 443096

	k = ((xo**3) - (yo**2)) * (inversoModular(xo, p))
	k = exponenciacionModulo(k, 1, p)

	cumplen = False

	#7. checar que se cumpla lo siguiente:

	res1 = (k**((p - 1)//4))
	res1 = exponenciacionModulo(res1, 1, p)

	res2 = (k**((p - 1)//2))
	res2 = exponenciacionModulo(res2, 1, p)

	if(res1 != 1 and res2 == 1):
		cumplen = True
	
	#x1 = alfa(xo, yo)
	#y1 = alfa(xo, yo)

	print(xo, yo)
	#8. si se cumple calcular (q - 1) alfa = x1, y1
	#si no, generar otro xo y yo

	x1 = xo
	y1 = p - yo

	#9 si se cumple lo siguiente se genera la curva
	#y ** 2 = x**3 - kx mod p
	#con generador (xo, yo)

	if(x1 == xo and y1 == p - yo and cumplen):
		todas = True

print("a: {}   b: {}   p: {}     q:{}     k:{}".format(a , b, p, q, k))
print("Curva Eliptica: y^2 = x3 -{}x mod {}".format(k, p))
print("punto generador: {},{}".format(xo, yo))

#Segunda parte
#y**2 = x**3 -kx mod p

#Para distribuir las llaves:
#clave provada 1 < m < q-1
#clave publica m*alfa = Beta   alfa es elemento generador

#1. generar k al azar menor que q - 1 y mayor q 1

#CIFRADO:

k = xo = random.randint(2, q - 2)
L = xo = random.randint(2, q - 2)

#LxAlfa = (xo, yo)
#Calculamos:

#y1 = k*alfa
#y2 = (xo, yo) + kBeta

#ek(xo, yo) = (y1, y2) ----- son los que se envían
#dk ===>
	#y2 - my1
	#[(xo, yo) + kBeta] - m(kAlfa)
	#[(xo,yo) + k(mAlfa)] - m(kAlfa)
	# (xo, yo)


#no supersingular: q mod p != 1
#no traza uno p != q
#no singular a(-k)^3  mod p != 0