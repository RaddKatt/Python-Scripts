"""
This program demonstrates iterating over a list of items and appending the count of items to a dictionary
Written in Python 3.5.1 on Mac
"""

def displayInventory(inventory):
	print('Inventory:')
	for item in inventory:
		print('\t- ' + str(inventory.get(item)) + ' ' + item)
		total = sum(inventory.values())
	print('\nTotal number of items: ' + str(total))

def addToInventory(inventory, addedItems):
	for item in addedItems:
		inventory.setdefault(item, 0)
		inventory[item] += 1
	return inventory

inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)
