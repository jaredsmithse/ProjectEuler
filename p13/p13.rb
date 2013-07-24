
sum = 0
File.open('p13_input.txt','r') do |infile|
	while (line = infile.gets)
		sum += line.to_i
	end
	puts sum.to_s[0..9]
end