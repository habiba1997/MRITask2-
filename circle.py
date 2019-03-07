

#circle1

width, height = 11, 11
a, b = 5, 5
r = 5
EPSILON = 2.2

map_ = [['.' for x in range(width)] for y in range(height)]

# draw the circle
for y in range(height):
    for x in range(width):
        # see if we're close to (x-a)**2 + (y-b)**2 == r**2
        if abs((x-a)**2 + (y-b)**2 - r**2) < EPSILON**2:
            map_[y][x] = '#'

 #print the map
for line in map_:
    print ' '.join(line)

# circle2

width, height = 7, 7
a, b = 3, 3
r = 3
EPSILON = 1.2

map_1 = [['.' for x in range(width)] for y in range(height)]

# draw the circle
for y in range(height):
    for x in range(width):
        # see if we're close to (x-a)**2 + (y-b)**2 == r**2
        if abs((x-a)**2 + (y-b)**2 - r**2) < EPSILON**2:
            map_1[y][x] = '#'

 #print the map
for line in map_1:
    print ' '.join(line)



