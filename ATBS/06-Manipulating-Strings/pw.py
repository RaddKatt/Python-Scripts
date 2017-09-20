#!/usr/local/bin/python

'''
An insecure password locker program
This program demonstrates the use of the pyperclip module to copy strings to the clipboard
Written with Python 2.7.12 on Mac
'''

PASSWORDS = {
	'email': 'Xy\GPt6!7CL}S7/_y:ev',
	'blog': 'WkgB,&EYTQCeP+N#e~7UYLFb5xqN_>',
	'luggage': '12345'
}

import sys, pyperclip

if len(sys.argv) != 2:
	print('Usage: ./pw.py [account] - copy account password')
	sys.exit()

account = str(sys.argv[1])	# first command line argument is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named \'' + account + '\'')
