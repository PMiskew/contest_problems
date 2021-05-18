'''
Modular Programming:

Description 

Benefits

Questions

'''

def sumSquareDifference(n):

	totalA = 0 #sum of squares
	totalB = 0 #sum squared


	for i in range(1, n + 1, 1):
		#Add to total A
		totalA = totalA + i*i
		totalB = totalB + i

	totalB = totalB * totalB #square total B outside loop

	difference = totalB - totalA
	print(difference)


def sumSquareDifferenceB(n):

	totalA = 0 #sum of squares
	totalB = 0 #sum squared


	for i in range(1, n + 1, 1):
		totalA = totalA + i*i
	
	for i in range(1, n + 1, 1):

		totalB = totalB + i

	totalB = totalB * totalB #square total B outside loop

	difference = totalB - totalA
	print(difference)

sumSquareDifference(10)





