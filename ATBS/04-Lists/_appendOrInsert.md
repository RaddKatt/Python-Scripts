# Add Values to Lists - append() & insert()
### Use the List methods append() and insert()

`append()` adds the argument to the _end of the list_:

```python
>>> spam = ['cat', 'dog', 'bat']
>>> spam
['cat', 'dog', 'bat']
>>> spam.append('moose')
>>> spam
['cat', 'dog', 'bat', 'moose']
```
`insert()` can add the value to _any_ index within the list:

```python
>>> spam = ['cat','dog','bat']
>>> spam
['cat', 'dog', 'bat']
>>> spam.insert(1,'moose')
>>> spam
['cat', 'moose', 'dog', 'bat']
```
