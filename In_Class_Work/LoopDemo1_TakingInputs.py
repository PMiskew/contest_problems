'''
This demo program shows how to loop an input until the user enters a value input

In the case of taking inputs and checking if valid a while is better because
this is a sitauton where you DO NOT know in advnace how many times it will run
'''

value = -1

while (value < 0 or value > 10):
	
	value = input("What is the value")
	value = int(value)
	
	if (value < 0 or value > 10):
		print("INVALID - TRY AGAIN")

print("THANK YOU")