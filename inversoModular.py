# regresa inverso modular de a modulo m
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
  
if __name__ == '__main__':
	a = int(input('Num: '))
	m = int(input('Modulo: '))
	print("Modular multiplicative inverse is", inversoModular(a, m)) 