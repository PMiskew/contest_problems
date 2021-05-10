#Step 1:  I need to write a loop that goes from 1 to 999 inclusive
'''
for i in range(1,1000,1):
	print(i)

'''

#Step 2: How do I check if a number is a multiple of 3 or 5
#			We do this using the % operator.  If a % b == 0 then a is a multiple 
#			of b or b is a factor of a

'''
x = input()
x = int(x) #cast x to an integer

if (x % 3 == 0):
	print(x,"is a factor of 3")
if (x % 5 == 0):
	print(x,"is a factor of 5")
'''

#Step 3: We need to check if a nubmber is a factor of 5 or 3

#or 
#A B A or B
#0 0   0
#0 1   1
#1 0   1
#1 1   1

'''
x = input()
x = int(x) #cast x to an integer


if (x % 3 == 0 or x % 5 == 0):
	print(x,"is a factor of 3 and/or 5")
'''

#Step 4: We need to make sum - this is an example of how to write a running sum

'''
total = 0

for i in range(0, 11,1):
	total = total + i

print(total)
'''


#Step 5: Put it all together
# 			This highlights the classic structure
#
#			Loop
#				Condition

total = 0

for i in range(1, 10,1):

	if (i % 3 == 0 or i % 5 == 0):

		total = total + i


print(total)



