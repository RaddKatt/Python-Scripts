#!/usr/local/bin/python

'''
bulletPointAdder.py - Adds Wikipedia bullet points to the start
of each line of text on the clipboard
Written with Python 2.7.12 on Mac
'''

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):	# loop through all indexes in the "lines" list
	lines[i] = '* ' + lines[i]	# add star to each string in the "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
