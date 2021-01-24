#https://www.nayuki.io/res/dwite-programming-contest-solutions/dwite-200410-p2.pdf

#Step 1: Take our input
#Key Idea: Fixed length string

time = input()

'''
01234
09:30

'''

#Step 2: Break up String
h = time[0:2] #inclusive:excusive 2 - 0 = 2
h = int(h) #casts to integer "09" --> 9

m = time[3:5]

#Step 3: Process AM PM situation
timeOfDay = "AM"

if (h > 12):
	timeOfDay = "PM"
	h = h - 12 
if (h == 0):
	h = 12

print(str(h)+":"+m+" "+timeOfDay)


