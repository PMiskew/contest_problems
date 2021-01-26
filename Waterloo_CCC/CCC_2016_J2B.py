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

#INPUT LINE
line1 = input()
row1 = line1.split(" ")
'''
row1 = [int(i) for i in row1] 
print(row1)
#'''

#CAST TO INT
for i in range(0, len(row1),1):
	row1[i] = int(row1[i])

line2 = input()
row2 = line2.split(" ")

for i in range(0, len(row2),1):
	row2[i] = int(row2[i])


line3 = input()
row3 = line3.split(" ")

for i in range(0, len(row3),1):
	row3[i] = int(row3[i])


line4 = input()
row4 = line4.split(" ")

for i in range(0, len(row4),1):
	row4[i] = int(row4[i])

'''
		  0	  1	  2	  3 
row1 =	[ 16,  3,  2, 13]
row2 =  [  5, 10, 11,  8]
row3 =  [  9,  6,  7, 12]
row4 =  [  4, 15, 14,  1]

'''



sr1 = row1[0] + row1[1] + row1[2] + row1[3]
sr2 = row2[0] + row2[1] + row2[2] + row2[3]
sr3 = row3[0] + row3[1] + row3[2] + row3[3]
sr4 = row4[0] + row4[1] + row4[2] + row4[3]

sc1 = row1[0] + row2[0] + row3[0] + row4[0]
sc2 = row1[1] + row2[1] + row3[1] + row4[1]
sc3 = row1[2] + row2[2] + row3[2] + row4[2]
sc4 = row1[3] + row2[3] + row3[3] + row4[3]


if (sr1 == sr2 and sr1 == sr3 and sr1 == sr4 and sr1 == sc1 and sr1 == sc2 and sr1 == sc3 and sr1 == sc4):
	print("magic")
else:
	print("not magic")

	