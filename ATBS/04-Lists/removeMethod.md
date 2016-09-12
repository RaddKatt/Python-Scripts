# Remove value from a List

`remove()` method - use when you know the value to be removed. `remove()` will delete the first match of that value from the list.

```python
>>> myList = ['coffee', 'tea', 'soda', 'beer']
>>> myList
['coffee', 'tea', 'soda', 'beer']
>>> myList.remove('soda')
>>> myList
['coffee', 'tea', 'beer']
```

`del` statement - use when you know the index of the value to be removed. `del` will delete the value at that index from the list.

``` python
>>> myList = ['coffee','tea','soda','beer']
>>> myList
['coffee', 'tea', 'soda', 'beer']
>>> del myList[2]
>>> myList
['coffee', 'tea', 'beer']
```

More Info: https://docs.python.org/3/tutorial/datastructures.html
