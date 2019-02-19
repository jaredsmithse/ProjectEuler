def is_palindrome(num):
	str_num = str(num)
	if len(str_num) % 2 == 0:
		
		first = str_num[0:len(str_num)/2]
		second = str_num[(len(str_num) / 2):]

		if first == second[::-1]:
			return True
		return False
	
	else:

		first = str_num[0:len(str_num)/2+1]
		second = str_num[len(str_num) / 2:]
		
		if first == second[::-1]:
			return True
		return False


def largest_three_digit_palindrome():
	palindromes = []
	for i in range(111,999):
		for j in range(111,999):
			if is_palindrome(i*j):
				palindromes.append(i*j)
	return sorted(palindromes)[-1]


print largest_three_digit_palindrome()
