"""
This program demonstrates using the setdefault() method to ensure that a key exists.
Written in Python 3.5.1 on Mac
"""

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
