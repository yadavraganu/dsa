matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Print the matrix
for row in matrix:
    print(row)
shift = ((0,1), (1,0), (0,-1), (-1,0))

x,y = 0,0
for i in range(16):
    