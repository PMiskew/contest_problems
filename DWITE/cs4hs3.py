#input

data = input() 
points = data.split(" ")
print(points)


topx = int(points[0])
topy = int(points[1])
bottomx = int(points[2])
bottomy = int(points[3])

width = bottomx - topx
height = bottomy - topy

print(width)
print(height) 

tall = 