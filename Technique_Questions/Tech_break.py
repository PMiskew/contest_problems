#What is the point of a break statement
#A break statement will break out of the most immediate loop that you are in


word = "ABCDEFG"
for i in range(0, len(word), 1):

	if (word[i] == 'C'):
		break;

	print(word[i])

#Break jumps to here and keeps going. 