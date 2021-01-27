#https://cemc.uwaterloo.ca/contests/computing/2017/stage%201/juniorEF.pdf

def problem():

	x = int(input())
	y = int(input())

	if (x > 0 and y > 0):
		return 1
	elif (x < 0 and y > 0):
		return 2
	elif (x < 0 and y < 0):
		return 3
	elif (x > 0 and y < 0):
		return 4


result = problem()
print(result)