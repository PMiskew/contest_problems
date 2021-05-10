'''
A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit 
numbers.

'''
def isPrime(n):

	for i in range(2,int(n**0.5),1):
		if (n % i == 0):
			return False

	return True

print(isPrime(101))
print(isPrime(23))
print(isPrime(24))
print("*****************")

def isPalindrome(n):

	n = str(n)
	for i in range(0,int(len(n)/2), 1):
		if (n[i] != n[len(n) - 1 - i]):
			return False

	return True;

print(isPalindrome(9009))
print(isPalindrome(90109))
print(isPalindrome(8009))
print(isPalindrome(9029))


def palindromePrime():

	pp = [] 

	i = 999
	j = 999

	while (i > 99):
		j = 999

		while (j > 99):

			p = i * j

			if (isPalindrome(p)):

				pp.append(p)

			j = j - 1

		i = i - 1

	pp.sort()
	return pp


		
	



print(palindromePrime())