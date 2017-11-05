#!/usr/local/bin/python3

'''
A phone number–finding program.
Accomplishes the same task as the previous exercise
But does so more easily using regular expressions
Written in Python 3.5.2 on Mac
'''

# Import the regex module
import re

if __name__ == "__main__":
	## Create a Regex object that matches a phone number pattern
	## the 'r' makes the string a raw string
	## so you don't have to escape backslashes using '\\d'
	phoneNumRegex = re.compile(r'(\d{3}-){2}\d{4}')
	
	## Use the Regex search method
	## to search for a match object
	## and store the result to 'mo'
	mo = phoneNumRegex.search('My number is 415-555-4242.')
	if mo is not None:
		## Return the match
		print('Phone number found: %s' % mo.group())
	else:
		## Report no matches were found
		print('No phone number was found.')
