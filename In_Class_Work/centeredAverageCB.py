'''
Big Idea:  If you modify a passed array/list you need to be very carful because
it is a reference type. 

When you pass primitive types, that is integers, strings, booleans a whole new copy
is made in memory

Memory

Start of Function call
 x   nums
 9   9


END of Function call
 x   nums
 9   10
'''
#Example 1
def doThis(a):


	a = a + 1
	
x = 9
doThis(x)
print(x) #This will print 

'''
Since lists are REFERENCE types we do not copy the data but pass a reference
to where it is in memory

MEMORY

arr -------> [4,5,100,1,6]
			  ^
			  \
nums ---------\

'''
#Example 2:
def doThat(nums):
	nums[0] = 99

arr = [4,5,100,1,6]
doThat(arr)
print(arr)



def centeredAverageA(nums):
	
	nums.sort()
	total = sum(nums)
	average = (total - nums[0] - nums[len(nums) - 1])/(len(nums) - 2)
	return average

arr1 = [4,5,100,1,6]
result = centeredAverageA(arr1)
print(result)
print(arr1)


def centeredAverageB(nums):

	#When finding the largest or smallest value of a list always
	#set it to a value in the list. 
	smallest = nums[0]
	largest = nums[0]
	total = 0;

	for i in range(0, len(nums),1):
		
		if (smallest > nums[i]):
			smallest = nums[i]

		if (largest < nums[i]):
			largest = nums[i]

		total = total + nums[i]

	average = (total - smallest - largest)/(len(nums) - 2)

	return average

arr2 = [4,5,100,1,6]
result = centeredAverageB(arr2)
print(result)
print(arr2)








