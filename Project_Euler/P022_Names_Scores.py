f = open("P022_names.txt","r")

s = f.read()

l = s.split(",")
l.sort()

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
score = 0
for i in range(0, len(l),1):

	
	l[i] = l[i].replace("\"","")
	
	
	tscore = 0;

	for j in range(0, len(l[i]),1):
		tscore = (letters.index(l[i][j]) + 1) + tscore

	score = score + (i+1)*tscore


print(score)