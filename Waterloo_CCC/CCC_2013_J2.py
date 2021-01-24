
def problem():
	#Step 1: Take our input

	word = input()

	#Step 2: loop through and check each letter

	for i in range(0, len(word),1):

		if (word[i] != "I" and  word[i] != "O" and word[i] != "S" and word[i] != "H" and word[i] != "Z" and word[i] != "X" and word[i] !=  "N"):
			return "NO"

	return "YES"


def problemALT():


	word = input()

	word = word.replace("I","")
	word = word.replace("O","")
	word = word.replace("S","")
	word = word.replace("H","")
	word = word.replace("Z","")
	word = word.replace("X","")
	word = word.replace("N","")

	if (len(word) == 0):
		return "YES"

	return "NO"

print(problemALT())









