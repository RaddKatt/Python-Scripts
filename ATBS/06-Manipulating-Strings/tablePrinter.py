#!/usr/local/bin/python

'''
This program demonstrates
Written with Python 2.7.12 on Mac
'''

tableData = [
	['apples', 'oranges', 'cherries', 'banana'],
	['Alice', 'Bob', 'Carol', 'David'],
	['dogs', 'cats', 'moose', 'goose']
]
longest = 0

def printTable(table):
	print(len(table))
	colWidths = [0] * len(table)
	print colWidths

	for i in range(0,len(table)):
		for item in table[i]:
			if len(item) > longest:
				longest = len(item)
	print(longest)

printTable(tableData)
