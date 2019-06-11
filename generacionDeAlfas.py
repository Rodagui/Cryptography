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

def multiplicacionModulo(a, b, mod):
	x = 0
	y = a % mod

	while b > 0:
		if b % 2 == 1:
			x = (x + y) % mod

		y = (y * 2) % mod
		b = b // 2

	return x % mod

primo = int(input("primo: "))
modulo = int(input("mod: "))

# y^2 = x^3 + ax + b
# para la curva eleiptica valida en cripto el valor de a = -k  
a = int(input("a: "))
#b = int(input("b: "))

print('(x1, y1) : ')

x1 = int(input())
y1 = int(input())

print('(x2, y2) : ')

x2 = int(input())
y2 = int(input())

lamda = 0
inverso = 0

equis = []
ye = []

equis.append(0)
ye.append(0)

equis.append(x1)
ye.append(y1)

if(x1 == x2 and y1 == y2):
	inverso = inversoModular((2*y1), modulo)
	#print(inverso)
	lamda = multiplicacionModulo(((3*x1**2) + a) , inverso, modulo)

	x3 = (lamda**2) - 2 * x1
	x3 = exponenciacionModulo(x3, 1, modulo)

	y3 = (lamda*(x1 - x3)) - y1;
	y3 = exponenciacionModulo(y3, 1, modulo)
else:
	lamda = (y2 - y1)*inversoModular((x2 - x1), modulo)
	lamda = exponenciacionModulo(lamda, 1, modulo)

	x3 = exponenciacionModulo(((lamda**2)-x1-x2), 1, modulo)
	y3 = exponenciacionModulo(((lamda*(x1-x3)) - y1), 1, modulo)

equis.append(x3)
ye.append(y3)

print(x3, y3)

pos = 0

for i in range(3, primo + 1):
	if(i % 2 == 0):
		pos = i // 2
		x1 = equis[pos]
		y1 = ye[pos]
		x2 = x1
		y2 = y1
		inverso = inversoModular((2*y1), modulo)
		#print(inverso)
		lamda = multiplicacionModulo(((3*x1**2) + a) , inverso, modulo)

		x3 = (lamda**2) - 2 * x1
		x3 = exponenciacionModulo(x3, 1, modulo)

		y3 = (lamda*(x1 - x3)) - y1;
		y3 = exponenciacionModulo(y3, 1, modulo)

	else:
		x1 = equis[1]
		y1 = ye[1]
		x2 = equis[i-1]
		y2 = ye[i-1]

		lamda = (y2 - y1)*inversoModular((x2 - x1), modulo)
		lamda = exponenciacionModulo(lamda, 1, modulo)

		x3 = exponenciacionModulo(((lamda**2)-x1-x2), 1, modulo)
		y3 = exponenciacionModulo(((lamda*(x1-x3)) - y1), 1, modulo)

	equis.append(x3)
	ye.append(y3)

print("-------------------")
for i in range(1 , len(equis)):
	print(equis[i], ye[i])

	#el 13avo ya vuelve a repetrise, entonces las alfas dependen del primo