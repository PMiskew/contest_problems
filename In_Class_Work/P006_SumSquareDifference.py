'''
Observations:

-	When we look at the values in the example they are increaseing by 1
	each time. 
		- Hints that Loop makes sense here. 

Trace Example

case where n = 10
 i	|	i < 11	| totalB
-----------------------------
 1  |  1 < 11 T |  0 + 1 = 1
 2. |  2 < 11 T |  1 + 2 = 3
 3. |. 3 < 11 T.|  3 + 3 = 6
 4. |  4 < 11 T |  6 + 4 = 10
 5. |  5 < 11 T |  10 + 5 = 15
 6. |  6 < 11 T.|  15 + 6 = 21
 7  |  7 < 11 T |  21 + 7 = 28
 8  |  8 < 11 T |  28 + 8 = 36
 9  |  9 < 11 T |  36 + 9 = 45
 10 | 10 < 11 T |  45 + 10 = 55
 11 | 11 < 11 F | EXIT LOOP



'''
totalA = 0 #sum of squares
totalB = 0 #sum squared


#Standard Python loop to go from 1 to 10
for i in range(1, 101, 1):
	#Add to total A
	totalA = totalA + i*i
	totalB = totalB + i

totalB = totalB * totalB #square total B outside loop

difference = totalB - totalA
print(difference)




