'''
This program demonstrates the use of the isX string methods 
Written with Python 2.7.12 on Mac
'''

while True:
	age = raw_input('Enter your age: ')
	if age.isdigit():
		break
	print('Please enter a number for your age.')

while True:
	password = raw_input('Select a new password (letters and numbers only):')
	if password.isalnum():
		break
	print('Passwords can only have letters and numbers.')
