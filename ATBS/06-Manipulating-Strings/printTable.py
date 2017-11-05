#!/usr/local/bin/python

## Written in Python 3.5.1 on Mac

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
	colWidths = [0] * len(tableData)
	newTable = []
	x = 0

	for i in tableData:
		if len(i) > x:
			x = len(i)

	for i in range(len(tableData)):
		highest = len(max(tableData[i], key=len))
		colWidths[i] = highest

	for i in range(x):
		newTable.append([])
		for j in range(len(tableData)):
			newTable[i].append(tableData[j][i].rjust(colWidths[j]))

	for i in newTable:
		print(' '.join(i))

if __name__ == "__main__":
	printTable()
