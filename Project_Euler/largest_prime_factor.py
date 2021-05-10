def factorList(n):

	fl = []

	for i in range(1,n+1,1):

		if (n%i == 0):
			fl.append(i)

	return fl

def factorListR(n,i,fl):

	if (i <= n):

		if (n % i == 0):
			fl.append(i)

		factorListR(n, i + 1,fl)


print(factorList(12))
fl = []
factorListR(12,1,fl)
print(fl)