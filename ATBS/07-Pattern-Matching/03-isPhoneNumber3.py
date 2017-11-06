#!/usr/local/bin/python3

'''
More examples of Regex searching,
grouping using parenthesis, and the groups() method
'''

# Import the regex module
import re

if __name__ == "__main__":
	## Create a Regex object that matches a phone number pattern
	## The 'r' makes the string a raw string
	## Each set of parenthesis is a new capture group
	phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
	
	## Use the Regex search method
	## to search for a match object
	## and store the result to 'mo'
	mo = phoneNumRegex.search('My number is 415-555-4242.')
	
	print('\nlen(mo.group()): %s' % len(mo.group()))
	print('mo.group(): %s' % mo.group())
	print('mo.group(1): %s' % mo.group(1))
	print('mo.group(2): %s\n' % mo.group(2))
	print('len(mo.groups()): %s' % len(mo.groups()))
	print('mo.groups(): ' + str(mo.groups()))
	
	## Use the multiple-assignment trick
	## to assign each value to a separate variable
	areaCode, mainNumber = mo.groups()
	print('Area Code: %s' % areaCode)
	print('Main Number: %s\n' % mainNumber)
