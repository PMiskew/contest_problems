'''

SHINS --> YES

Simplify Problem:  Check to ensure string
only has I, O, S, H, Z, X and N


Basic Approach: 

	Loop thorugh every letter of string.
	Check to ensure every letter is one of the valid letters

Observe: 
	In order to say yes I must check every letter!
	As soon as I find a "bad letter" I can say NO


'''

def approach1():

	value = input()

	#Critical Idea: How to loop through a string
	'''		
	Trace:
	value = SHINS

	i |	 	i < len(value) 		| 
	0 |		0 < 5 T 
	1 |		1 < 5 T
	2 |	 	2 < 5 T
	3 |  	3 < 5 T
	4 |		4 < 5 T
	5 |  	5 < 5 F EXIT LOOP



	'''
	for i in range(0, len(value), 1):

		if value[i] != 'I' and value[i] != 'O' and value[i] != 'S' and value[i] != 'H' and value[i] != 'Z' and value[i] != 'X' and value[i] != 'N':
			return "NO"

	return "YES"


#result = approach1()
#print(result)



#Change the for loop to a while loop
def approach2():



	value = input()

	i = 0

	#Conditional Loops are best when we don't know in advance how 
	#many times the loop will run - Taking an input that the user
	#might input something bad. 

	#Counted Loops are best when we know in advance how many 
	#times the loop will run. 

	while i < len(value):

		if value[i] != 'I' and value[i] != 'O' and value[i] != 'S' and value[i] != 'H' and value[i] != 'Z' and value[i] != 'X' and value[i] != 'N':
			return "NO"

		i = i + 1


	return "YES"


'''

We can use the replace method to "collapse" a string


'''
def approach3():



	value = input()

	value = value.replace("I","") #This will replace all S with empty
	value = value.replace("O","") #This will replace all S with empty
	value = value.replace("H","") #This will replace all S with empty
	value = value.replace("Z","") #This will replace all S with empty
	value = value.replace("X","") #This will replace all S with emptyvalue = value.replace("H","") #This will replace all S with empty
	value = value.replace("S","") #This will replace all S with empty
	value = value.replace("N","") #This will replace all S with empty
	

	#The result will be that the string is empty
	if len(value) == 0:
		return "YES"
	return "NO"


result = approach3()
print(result)






