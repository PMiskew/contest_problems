
def problem():
	num = input()
	num = int(num)


	#Hard code:
	'''
	We can map out all possibilities
	10 	- (5,5)
	9 	- (5,4)
	8	- (4,4),(5,3)
	7	- (5,2),(4,3)
	6	- (5,1),(4,2),(3,3)
	5	- (5,0),(4,1),(3,2)
	4 	- (4,0),(3,1),(2,2)
	3	- (3,0),(2,1)
	2	- (2,0),(1,1)
	1	- (1,0)


	'''

	if (n == 10 or n == 9 or n == 1):
		print(1)
	elif (n == 8 or n == 7 or n == 3 or n == 2):
		print(2)
	elif (n == 6 or n == 5 or n == 4):
		print(3)


problem()