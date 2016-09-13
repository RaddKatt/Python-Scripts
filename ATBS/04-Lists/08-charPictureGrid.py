# This program demonstrates the use of nested loops
# to invert a nested list
# Written in Python 3.5.1 on Mac

grid = [['.','.','.','.','.','.'],
['.','O','O','.','.','.'],
['O','O','O','O','.','.'],
['O','O','O','O','O','.'],
['.','O','O','O','O','O'],
['O','O','O','O','O','.'],
['O','O','O','O','.','.'],
['.','O','O','.','.','.'],
['.','.','.','.','.','.']]

print('\n=========')

for i in range(0,len(grid)):
    newGrid = ''
    for j in range(0,len(grid[0])):
        newGrid += grid[i][j]
    print(newGrid)

print('\n=========\n')

for i in range(0,len(grid[0])):
    newGrid = ''
    for j in range(0,len(grid)):
        newGrid += grid[j][i]
    print(newGrid)

print('\n=========\n')
