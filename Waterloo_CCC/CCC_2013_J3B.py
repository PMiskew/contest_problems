

#This lists is essentially a histogram
nums = [0,0,0,0,0,0,0,0,0,0]

num = int(input())

#Loop through num and check each digit adn update nums
#Notice that the numbers and index's match. 


#Loop through nums and if you see a number other than 0 or 1 it is fail. 

while (num != 0):
	i = num%10
	nums[i] = nums[i] + 1
	num = num//10

distinct = True
for i in range(0,len(nums),1):
	if (nums[i] > 1):
		distinct = False

if distinct == True
	print("DISTINCT")
else:
	print("NOT DISTINCT")

'''
345
num != 0 True
	i = 5
	num = 34
	nums = [0,0,0,0,0,1,0,0,0,0]
num != 0 True
	i = 4
	num = 3
	nums = [0,0,0,0,1,1,0,0,0,0]
num != 0 True
	i = 3
	num = 0
	nums = [0,0,0,1,1,1,0,0,0,0]
num != FALSE
EXIT LOOP






'''