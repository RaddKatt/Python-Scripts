#!/usr/local/bin/python

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

	for i in range(0, x):
		newTable.append([])

	for i in range(0, len(tableData)):
		highest = len(max(tableData[i], key=len))
		colWidths[i] = highest

	for i in range(0, x):
		for j in range(0, len(tableData)):
			newTable[i].append(tableData[j][i].rjust(colWidths[j]))

	for i in newTable:
		print(' '.join(i))

if __name__ == "__main__":
	printTable()
