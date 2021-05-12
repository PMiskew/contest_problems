#Input
#Take in 4 integer values
a = input() #assignment statements
a = int(a) #self-referencing assignment statement 

b = input()
b = int(b)

c = input()
c = int(c)

d = input()
d = int(d)


#Process
#Compare them to look for a pattern
state = "No Fish"

if (a == b and b == c and c == d):
	state = "Fish At Constant Depth"
elif (a < b and b < c and c < d):
	state = "Fish Rising"
elif (a > b and b > c and c > d):
	state = "Fish Diving"

#Output
#Outputs 1 of 4 statements. 
print(state)