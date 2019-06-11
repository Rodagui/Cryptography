def gcd(a, b):
	if( b == 0):
		return a
	else:
		return gcd(b, a % b)

print(gcd(3355851383, 3355851384))
