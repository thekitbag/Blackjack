def divisors(number):
# gives all of the factors of the given number
	results = []
	for i in range(2,number):
		if number % int(i) == 0:
			results.append((i))
	return results

print divisors(12345)
