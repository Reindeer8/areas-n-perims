"""
AREAS AND PERIMETERS

Write a program that constructs a figure given its area A and perimeter P. 
The figure should be embedded into a rectangular matrix 
consisting of RxC fields where each field can be either 
full (denoted by #) or empty (denoted by . or _ or space).

The area of a figure is the total number of filled fields. 
The perimeter is the number of edges between two fields, 
one of which is full and the other empty (or outside the matrix). 
All edges are either horizontal or vertical, no curved edges are allowed.

For example, the following figure has an area of 2 and perimeter of 8.
.#
#.
and
###
#.#
###
has an area of 8 and a perimeter of 16.

You don't have to create the same figure as in the examples. 
You can choose the dimensions RxC, however, 
the matrix must fit in the memory and be printable within the time limit.

Your program should output the chosen dimensions 
on the first line (R and C) 
and then R lines, each of C characters representing the matrix; 
or determine that no solution exists.
"""

def layout(area, perim):
    
    # checking if there is a solution with the inputs
    if perim % 2 != 0 or perim > area * 4 or perim < (area ** 0.5) * 4:
        return None

    touching_sides = area * 4 - perim
    con = []
    disc = []

    # drawing squares that are not connected
    if touching_sides == 0:
        singles = area        
    else:
        singles = area - (touching_sides // 2 + 1)    
    for i in range(singles):        
        disc.append('.')
        disc.append('#')
        area -= 1
        perim -= 4
    if area == 0:
        return disc[1:]
    
    # drawing squares that are connected to the main body
    sideab = perim // 2
    c = 1
    while abs(c * (sideab - c)) < area:        
        c+=1
    max_len = c
    while True:
        while (c - 1) * (sideab - max_len) < area:
            con.append('#' * c + (max_len-c) * '.')
            area -= c
            if area <= 0:
                return con + disc
            sideab -= 1            
        c -= 1        

test_cases = [[3, 10],[2, 8],[6, 14],[7, 18],[8, 14], [4, 101], [9, 12], [5, 10], [1, 1], [11, 14], [42,28]]

for area, perim in test_cases:
    print(f'Input:\nA={area}, P={perim} \nOutput:')
    a = layout(area, perim)        
    if a:
        print(f'{len(a)} {len(a[0])}')
        print(*a, sep = '\n', end = '\n\n')
    else:
        print('No solution exists\n')
