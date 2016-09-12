# Sorting values in a list
Use the `sort()` List method.

```python
>>> myList = [8,6,5,3.14,2,-4]
>>> myList.sort()
>>> myList
[-4, 2, 3.14, 5, 6, 8]
```

```python
myList = ['dogs','cats','kittens','bears']
>>> myList.sort()
>>> myList
['bears', 'cats', 'dogs', 'kittens']
```

```python
# sort in reverse order
>>> myList
['bears', 'cats', 'dogs', 'kittens']
>>> myList.sort(reverse=True)
>>> myList
['kittens', 'dogs', 'cats', 'bears']

>>> myList = [3,6,1,8,10,2]
>>> myList.sort(reverse=True)
>>> myList
[10, 8, 6, 3, 2, 1]
```

```python
# Example of how sort() uses "ASCIIbetical order"
# This will treat all values as lowercase without actually changing the case.
>>> myList = ['cat','Ant','Claw','apple']
>>> myList.sort()
>>> myList
['Ant', 'Claw', 'apple', 'cat']

# Correct by using 'key=str.lower'
>>> myList
['Ant', 'Claw', 'apple', 'cat']
>>> myList.sort(key=str.lower)
>>> myList
['Ant', 'apple', 'cat', 'Claw']
```
