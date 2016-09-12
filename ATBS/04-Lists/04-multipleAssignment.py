# This program demonstrates use of the Multiple Assignment Trick
# Written in Python 3.5.1 on Mac

# Instead of doing this:
cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

# You could use the Multiple Assignment Trick:
cat = ['fat', 'black', 'loud']
size, color, disposition = cat

# Keep in mind that the number of variables and the length
# of the list must be exactly equal,
# or Python will give you a ValueError:
#
# >>> cat = ['fat', 'black', 'loud']
# >>> size, color, disposition, name = cat
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# ValueError: not enough values to unpack (expected 4, got 3)
