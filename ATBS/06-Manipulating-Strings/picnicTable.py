'''
This program demonstrates the use of the ljust, rjust, and center string methods
Written with Python 2.7.12 on Mac
'''

def printPicnic(itemsDict, leftWidth, rightWidth):
	print(' PICNIC ITEMS '.center(leftWidth + rightWidth, '-'))
	for k, v in itemsDict.items():
		print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {
	'sandwiches': 4,
	'apples': 12,
	'cups': 4,
	'cookies': 8000
}

printPicnic(picnicItems, 12, 6)
printPicnic(picnicItems, 20, 6)
printPicnic(picnicItems, 50, 6)
