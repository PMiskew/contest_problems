def getFactors(n):

	result = []

	for i in range(1,n, 1):
		if (n % i == 0):
			result.append(i)

	return result

'''
-1 deficite
 0 perfect
 1 abundant 
'''
def isPerfectNumber(n):

	factors = getFactors(n)

	total = sum(factors)

	if (total == n):
		return 0
	elif total < n:
		return -1
	return 1	


numbers = [0, 6, 28, 496, 8128]

'''
for i in range(0,28132,1):
	if isPerfectNumber(i) == 0:
		numbers.append(i)
'''



print(numbers)
