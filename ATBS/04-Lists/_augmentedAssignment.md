| Augmented Assignment Statement | Equivalent Assignment Statement |
| ------------------------------ | ------------------------------- |
| spam += 1                      | spam = spam + 1                 |
| spam -= 1                      | spam = spam - 1                 |
| spam *= 1                      | spam = spam * 1                 |
| spam /= 1                      | spam = spam / 1                 |
| spam %= 1                      | spam = spam % 1                 |

The `+=` operator can also do string and list concatenation, and the `*=` operator can do string and
list replication, such as below:

```python
>>> spam = 'Hello'
>>> spam += ' world!'
>>> spam
'Hello world!'
```

```python
>>> bacon = ['Zophie']
>>> bacon *= 3
>>> bacon
['Zophie', 'Zophie', 'Zophie']
```
