fib_sequence = [1,2]
sum = 0

def get_next_fib(array)
	return array[-1] + array[-2]
end

while get_next_fib(fib_sequence) <= 4000000
	fib_sequence << get_next_fib(fib_sequence)
end

fib_sequence.each do |num|
	if num % 2 == 0
		sum += num
	end
end

puts sum
