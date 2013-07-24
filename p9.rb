def has_root(num)
	return Math.sqrt(num) % 1 == 0
end

def is_triplet(f,s,t)
	if f*f + s*s == t*t
		return true
	elsif t*t + f*f == s*s
		return true
	elsif s*s + t*t == f*f
		return true
	else
		return false
	end
end

def find_triplet(num)
	(1..num).each do|f|
		(1..num).each do|s|
			(1..num).each do|t|
				if f + s + t == num
					if is_triplet(f,s,t)
						puts "#{f} #{s} #{t}"
						return f*s*t	
					end
				end
			end
		end
	end 
	return "not found"
end

puts find_triplet(1000)