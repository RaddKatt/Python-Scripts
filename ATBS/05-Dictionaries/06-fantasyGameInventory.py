"""
This program demonstrates iterating over a dictionary data structure
Written in Python 3.5.1 on Mac
"""

inv = {'arrow': 12, 'dagger': 1, 'gold coin': 42, 'rope': 1, 'torch': 6}

def displayInventory(inventory):
	print('Inventory:')
	for item in inventory:
		print('\t- ' + str(inventory.get(item)) + ' ' + item)
	total = sum(inventory.values())
	print('\nTotal number of items: ' + str(total))

displayInventory(inv)
