def findroot(s):

	start = 0
	end = 1

	'''

	abcddeffab
	
	s[start:end] --> a
	
	s[start:end] --> ab

	'''
	for i in range(0,len(s),1):
		#boolean expression
		#Bigger Idea: And are short circuited 
		#	AND - 	If the first condition fails the rest is ignored. This makes it possible
		#			to do lenght checks and have possible index out of bounds issues by
		#			always doing the length check first
		#			

		#			word = <some word lenght unknown>
		#			#check is first three letters are bob
		
		#			#This is all prdicated on the precondition that len(word) > 2
		#			if (word[0:3] == "bob"):
		#				print("The first three letters spell bob")

		#			if (len(word)> 2):
		#				if (word[0:3] == "bob"):
		#					print("The first three letters spell bob")

		#			#WORKS BECAUSE OF SHORTCIRCUITING
		#			if (len(word) > 2 and word[0:3] == "bob"):
		#				print("The first three letters spell bob")

		#			#FAILS BECAUSE OF INDEX OUT OF BOUNDS
		#			if (word[0:3] == "bob" and len(bob) > 2):
		#				print("The first three letters spell bob")

		#	OR	- If the first condition is TRUE then it doesn't check the second condidion
		#
		result = len(s) % len(s[start:end]) == 0 and s.count(s[start:end]) == len(s)/len(s[start:end])

		if (result == True):
			print(s[start:end])
			return #You can just return to exit a function
		end = end + 1

	print(s)


file = open("DATA1cs4hs1.txt","r")

data = file.read().split("\n")


for i in range(0, len(data), 1):
	findroot(data[i])


