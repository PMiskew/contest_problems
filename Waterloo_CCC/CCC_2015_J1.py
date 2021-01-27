#https://www.cemc.uwaterloo.ca/contests/computing/2015/stage%201/juniorEn.pdf
'''
This question is highlighting the importance of the order in which you
check conditions

'''

def problem():

	m = int(input())
	d = int(input())

	if (m > 2):
		return "After"
	elif (m == 2 and d > 18):
		return "After"
	elif (m < 2):
		return "Before"
	elif (m == 2 and d < 18):
		return "Before"

	return "Special"

print(problem())