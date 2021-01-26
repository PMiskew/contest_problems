def problem():

	#Step 1: Take inputs
	y = input()
	y = int(y)

	m = input()
	m = int(m)

	#Step 2: Find the difference between youngest and middle
	d = m - y # 15 - 12 = 3

	#Step 3: Find oldest by adding d to middle age
	o = m + d

	#Step 4: print out result
	print(o)

problem()

