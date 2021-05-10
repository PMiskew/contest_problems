
f1 = 1
f2 = 1
ctr = 2

while len(str(f2)) < 1000:
	temp = f1
	f1 = f2
	f2 = f2 + temp
	ctr = ctr + 1

print(ctr)