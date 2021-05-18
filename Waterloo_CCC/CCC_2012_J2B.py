'''
Description: How is this example differnet than the prervious

'''

def soundsFishy():
	#Input
	#Take in 4 integer values
	a = input() #assignment statements
	a = int(a) #self-referencing assignment statement 

	b = input()
	b = int(b)

	c = input()
	c = int(c)

	d = input()
	d = int(d)


	#Process
	#Compare them to look for a pattern


	if (a == b and b == c and c == d):
		print("Fish At Constant Depth")
		return
	elif (a < b and b < c and c < d):
		print("Fish Rising")
		return
	elif (a > b and b > c and c > d):
		print("Fish Diving")
		return
	print("No Fish")

soundsFishy()
