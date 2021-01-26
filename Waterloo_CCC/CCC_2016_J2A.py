#*******************************
'''
Visualization

i = index
r = row
c = column

        c i     c i     c i     c i 
r i		1(0)	2(1)	3(2)	4(3)
1(0)	r0c0,	r0c1, 	r0c2, 	r0c3
2(1)	r1c0,	r1c1, 	r1c2, 	r1c3
3(2)	r2c0, 	r2c1, 	r2c2, 	r2c3
4(3)	r3c0, 	r3c1, 	r3c2, 	r3c3 

'''
#*******************************
'''
r0c0 = 16
r0c1 = 3
r0c2 = 2
r0c3 = 13

r1c0 = 6
r1c1 = 10
r1c2 = 11
r1c3 = 8

r2c0 = 9
r2c1 = 6
r2c2 = 7
r2c3 = 12

r3c0 = 4
r3c1 = 15
r3c2 = 14
r3c3 = 1
#'''

#Take each input manually: Works with JAVA Scanner, not Python
r0c0 = int(input())
r0c1 = int(input())
r0c2 = int(input())
r0c3 = int(input())

r1c0 = int(input())
r1c1 = int(input())
r1c2 = int(input())
r1c3 = int(input())

r2c0 = int(input())
r2c1 = int(input())
r2c2 = int(input())
r2c3 = int(input())

r3c0 = int(input())
r3c1 = int(input())
r3c2 = int(input())
r3c3 = int(input())
#'''

sr1 = r0c0 + r0c1 + r0c2 + r0c3
sr2 = r1c0 + r1c1 + r1c2 + r1c3
sr3 = r2c0 + r2c1 + r2c2 + r2c3
sr4 = r3c0 + r3c1 + r3c2 + r3c3

sc1 = r0c0 + r1c0 + r2c0 + r3c0
sc2 = r0c1 + r1c1 + r2c1 + r3c1
sc3 = r0c2 + r1c2 + r2c2 + r3c2
sc4 = r0c3 + r1c3 + r2c3 + r3c3

if (sr1 == sr2 and sr1 == sr3 and sr1 == sr4 and sr1 == sc1 and sr1 == sc2 and sr1 == sc3 and sr1 == sc4):
	print("magic")
else:
	print("not magic")












