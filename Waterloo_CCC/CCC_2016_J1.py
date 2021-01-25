#https://www.cemc.uwaterloo.ca/contests/computing/2016/stage%201/juniorEn.pdf
def problemALT():

	games = []

	games.append(input())
	games.append(input())
	games.append(input())
	games.append(input())
	games.append(input())
	games.append(input())

	w = 0
	l = 0

	for i in range(0, len(games), 1):

		if (games[i] == "W"):
			w = w + 1
		else:
			l = l + 1

	#Step 3: Check the group
	if (w == 5 or w == 6):
		return 1
	elif (w == 3 or w == 4):
		return 2
	elif (w == 1 or w == 2):
		return 3

	return -1

print(problemALT())


def problem():

	#Step 1: Take inputs
	g1 = input()
	g2 = input()
	g3 = input()
	g4 = input()
	g5 = input()
	g6 = input()

	#Step 2: We need to count if an inputs is a win or loss
	w = 0
	l = 0

	if (g1 == "W"):
		w = w + 1
	else:
		l = l + 1

	if (g2 == "W"):
		w = w + 1
	else:
		l = l + 1

	if (g3 == "W"):
		w = w + 1
	else:
		l = l + 1

	if (g4 == "W"):
		w = w + 1
	else:
		l = l + 1

	if (g5 == "W"):
		w = w + 1
	else:
		l = l + 1

	if (g6 == "W"):
		w = w + 1
	else:
		l = l + 1

	#Step 3: Check the group
	if (w == 5 or w == 6):
		return 1
	elif (w == 3 or w == 4):
		return 2
	elif (w == 1 or w == 2):
		return 3

	return -1



#print(problem())





