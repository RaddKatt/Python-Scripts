# Removing values from a List

`remove()` method - Use when you know the value to be removed. `remove()` will delete the first match of that value from the list.

```python
>>> myList = ['coffee', 'tea', 'soda', 'beer']
>>> myList
['coffee', 'tea', 'soda', 'beer']
>>> myList.remove('soda')
>>> myList
['coffee', 'tea', 'beer']
```

`del` statement - Use when you know the index of the value to be removed. `del` will delete the value at that index from the list.

``` python
>>> myList = ['coffee','tea','soda','beer']
>>> myList
['coffee', 'tea', 'soda', 'beer']
>>> del myList[2]
>>> myList
['coffee', 'tea', 'beer']
```

`clear()` method - Use to remove all items from a list. Equivalent to `del myList[:]`.

```python
>>> myList = ['coffee','tea','soda','beer']
>>> myList
['coffee', 'tea', 'soda', 'beer']
>>> myList.clear()
>>> myList
[]
```

More Info: https://docs.python.org/3/tutorial/datastructures.html
