def sum_of_squares(num):
	sum = 0
	for i in range(1,num + 1):
		sum += i*i
	return sum

print sum_of_squares(10)

def square_of_sum(num):
	sum = 0
	for i in range(1,num + 1):
		sum += i
	return sum * sum

print square_of_sum(10)

def sum_square_difference(num):
	return square_of_sum(num) - sum_of_squares(num)

print sum_square_difference(100)