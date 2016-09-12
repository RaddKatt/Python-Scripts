# Make a duplicate copy of a mutable data type
### Using the `copy` module

import the `copy` module:

```python
import copy
```

- `copy()` function - Use for lists or dictionaries that **don't** contain inner lists or dictionaries.
```python
>>> import copy
>>> myList1 = ['a','b','c','d']
>>> myList2 = copy.copy(myList1)
>>> myList1
['a', 'b', 'c', 'd']

>>> myList2
['a', 'b', 'c', 'd']

>>> myList2[0] = 'z'
>>> myList2
['z', 'b', 'c', 'd'] # myList2 is an independent copy of myList1, not a reference to the same list

>>> myList1
['a', 'b', 'c', 'd'] # myList1 is unaffected by index change
```

- `deepcopy()` function - Use for lists or dictionaries that **do** contain inner lists or dictionaries.

```python
>>> import copy
>>> myList1.append(['sushi','edamame','sake'])
>>> myList1.append(['tacos','beans','beer'])
>>> myList2 = copy.deepcopy(myList1)
>>> myList1
[['sushi', 'edamame', 'sake'], ['tacos', 'beans', 'beer']]

>>> myList2
[['sushi', 'edamame', 'sake'], ['tacos', 'beans', 'beer']]

>>> myList2[0][0] = 'ramen'
>>> myList2
[['ramen', 'edamame', 'sake'], ['tacos', 'beans', 'beer']]
# myList2 is an independent copy of myList1, not a reference to the same list

>>> myList1
[['sushi', 'edamame', 'sake'], ['tacos', 'beans', 'beer']] # myList1 is unaffected by index change
```
