"""
This program demonstrates using pretty printing w/ the 'pprint' module
Written in Python 3.5.1 on Mac
"""

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
