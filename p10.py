from math import sqrt

def is_prime(num):
	if sqrt(num) % 1 == 0:
		return False

	max = int(round(sqrt(num)))
	for i in range(2,max +1):
		if num % i == 0:
			return False
	return True

def find_prime_sum(num):
	sum = 0
	for i in range(1,num):
		if is_prime(i):
			sum += i
	return sum

print find_prime_sum(2000000)