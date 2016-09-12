# This program demonstrates how List references work
# Written in Python 3.5.1 on Mac

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)

# Even though spam and someParameter contain separate references,
# they both refer to the same list
# This is why the append('Hello') method call inside the function
# affects the list even after the function call has returned.

# For immutable data types, Python stores the value itself
# For mutable data types, like lists and dictionaries,
# Python stores the reference to that value.
