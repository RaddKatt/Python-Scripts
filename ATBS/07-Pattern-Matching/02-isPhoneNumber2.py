#!/usr/local/bin/python3

'''
A phone number–finding program.
Accomplishes the same task as the previous exercise
Does so more easily using regular expressions
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
	mo = phoneNumRegex.search('My number is 415-555-4242.')
	if mo is not None:
		print('Phone number found: %s' % mo.group())
	else:
		print('No phone number was found.')
