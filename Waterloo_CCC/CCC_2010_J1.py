def problem():

	num = input()
	num = int(num)

	#Hard Code by checking all possibilies
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
	#'''

	if (num == 10 or num == 9 or num == 1):
		print(1)
	elif (num == 8 or num == 7 or num == 3 or num == 2):
		print(2)
	else:
		print(3)

problem()