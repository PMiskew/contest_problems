#https://www.cemc.uwaterloo.ca/contests/computing/2013/stage1/juniorEn.pdf

def isDistinct(x):

	nums = []

	while (x != 0):
		nums.append(x%10)
		x = x//10

	#Sort nums
	nums.sort()

	for i in range(1,len(nums),1):
		if (nums[i] == nums[i - 1]):
			return False

	return True



num = int(input()) #Take input
num = num + 1 #increase num by 1 since we are looking for the next number

distinct = isDistinct(num)

#loop while isDistinct returns false.  In the loop we increment 
#
while (distinct == False):
	num = num + 1
	distinct = isDistinct(num)

print(num)