#Step 1: take inputs
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

#Step 2: Find the distance between two points, which
#is the radius

r = ((y2-y1)**2+(x2-x1)**2)**(1/2)

#Step 3: take the distance and find area

a = 3.14159*r**2

#Step 3.5
a = a * 1000
a = round(a)
a = a/1000



#Step 4: print area
print(a)