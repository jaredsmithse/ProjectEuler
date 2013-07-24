from math import sqrt

def is_prime(num):
	if sqrt(num) % 1 == 0:
		return False

	max = int(round(sqrt(num)))
	for i in range(2,max +1):
		if num % i == 0:
			return False
	return True

def find_largest_prime_factor(max):
	factors = []
	num_left = max
	range_end = int(sqrt(num_left))
	while num_left != 1 :
		for i in range(2,range_end):
			if is_prime(i):
				if num_left % i == 0:
					factors.append(i)
					num_left = num_left/i
		range_end = int(sqrt(num_left))

	return factors[-1]

#600851475143   13195
print find_largest_prime_factor(600851475143)