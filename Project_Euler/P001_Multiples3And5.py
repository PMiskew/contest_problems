
def sumMultiplesA():
	total = 0

	for i in range(1, 10,1):

		if (i % 3 == 0 or i % 5 == 0):

			total = total + i


	print(total)


sumMultiplesA()

'''
In this version we return values instead of printing it
'''

def sumMultiplesB():
	total = 0

	for i in range(1, 10,1):

		if (i % 3 == 0 or i % 5 == 0):

			total = total + i


	return total


result = sumMultiplesB()
print(result)


def sumMultiplesC():
	total = 0

	num = input()
	num = int(num)

	for i in range(1, num,1):

		if (i % 3 == 0 or i % 5 == 0):

			total = total + i


	return total


result = sumMultiplesC()
print(result)


def sumMultiplesD(num):
	total = 0


	for i in range(1, num,1):

		if (i % 3 == 0 or i % 5 == 0):

			total = total + i


	return total


result = sumMultiplesD(10)
print(result)



def sumMultiplesE(num,a,b):
	total = 0


	for i in range(1, num,1):

		if (i % a == 0 or i % b == 0):

			total = total + i


	return total


result = sumMultiplesC()
print(result)




