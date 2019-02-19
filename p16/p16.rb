num = 2**1000
sum = 0
num.to_s.each_char do |digit|
	sum += digit.to_i
end
puts sum