# numero ^exp mod m
def exponenciacionModulo(num, exponente, mod):
	res = 1
	num %= mod
	
	while exponente > 0:
		if exponente % 2 == 1:
			res = res * num % mod
		
		num = num * num % mod

		exponente = exponente // 2

	return res

#a * b mod m
def multiplicacionModulo(a, b, mod):
	x = 0
	y = a % mod

	while b > 0:
		if b % 2 == 1:
			x = (x + y) % mod

		y = (y * 2) % mod
		b = b // 2

	return x % mod


#(a^p * b^q) mod m
def multiplicacionExponenteModulo(a, p, b, q, mod):
	m = exponenciacionModulo(a, p, mod)
	n = exponenciacionModulo(b, q, mod)

	return multiplicacionModulo(m, n, mod)

if __name__ == '__main__':
	print("\n")
	print("1. Exponenciacion modulo (-------  num ^exp mod m   -----)")
	print("2. Exponenciacion modulo (-------   a * b mod m   -----)")
	print("3. Exponenciacion modulo (-------  (a^p * b^q) mod m   -----)")
	print("\n")
	opcion = input("Opcion: ")

	print("\n")
	print("\n")
	if(opcion == '1'):

		num = int (input("num: "))
		exp = int(input("exp: "))
		mod = int(input("mod: "))

		print(exponenciacionModulo(num, exp, mod))

	if(opcion == '2'):

		a = int (input("a: "))
		b = int(input("b: "))
		mod = int(input("mod: "))

		print(multiplicacionModulo(a, b, mod))

	if(opcion == '3'):

		a = int (input("a: "))
		p = int (input("p: "))
		b = int (input("b: "))
		q = int (input("q: "))
		mod = int(input("mod: "))
		
		print(multiplicacionExponenteModulo(a, p, b, q, mod))