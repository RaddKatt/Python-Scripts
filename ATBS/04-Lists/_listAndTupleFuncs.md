# Converting Data types with `list()` & `tuple()`

`list()` examples:

``` python
>>> myTuple = ('doe', 'ray', 'me')
>>> type(myTuple)
<class 'tuple'>

>>> list(myTuple)
['doe', 'ray', 'me']

>>> type(list(myTuple))
<class 'list'>
```

``` python
>>> myString = 'Ben Franklin'
>>> type(myString)
<class 'str'>

>>> list(myString)
['B', 'e', 'n', ' ', 'F', 'r', 'a', 'n', 'k', 'l', 'i', 'n']

>>> type(list(myString))
<class 'list'>
```

`tuple()` examples:

``` python
>>> myList = ['a','b','c']
>>> type(myList)
<class 'list'>

>>> tuple(myList)
('a', 'b', 'c')

>>> type(tuple(myList))
<class 'tuple'>
```

``` python
>>> myString = 'John Rolfe'
>>> type(myString)
<class 'str'>

>>> tuple(myString)
('J', 'o', 'h', 'n', ' ', 'R', 'o', 'l', 'f', 'e')

>>> type(tuple(myString))
<class 'tuple'>
```
