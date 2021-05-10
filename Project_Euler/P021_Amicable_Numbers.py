def getFactors(n):

	result = []

	for i in range(1,n, 1):
		if (n % i == 0):
			result.append(i)

	return result

def sumFactors(n):

	total = 0;
	for i in range(1 ,n, 1):
		if (n % i == 0):
			total = total + i

	return total

def isAmicable(n):

	totalA = sumFactors(n)
	totalB = sumFactors(totalA)

	if totalB == n and totalA != totalB:
	
		return True

	return False


total = 0

for i in range(1, 10000,1):

	t =  isAmicable(i)

	if t:
		#print(i)
		total = total + i

print(total)


