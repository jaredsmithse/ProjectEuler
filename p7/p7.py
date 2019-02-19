def is_prime(num,list):
	for i in list:
		if num % i == 0:
			return False
	return True

def find_nth_prime(n):
	primes = [2]
	current_num = 3
	while len(primes) < n:
		if is_prime(current_num,primes):
			primes.append(current_num)
			current_num += 1
		else:
			current_num += 1
	return primes[-1]

print find_nth_prime(10001)