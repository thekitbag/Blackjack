#fibonacci sequence generator
def fib_gen(number):
#gives a fibonacci sequence of the stated length
	result = [1, 2]
	if number == 1:
		return 1
	elif number == 2:
		return [1,2]
	else:	
		for i in range(2,number):
			result.append(result[i-1]+result[i-2])
	return result

