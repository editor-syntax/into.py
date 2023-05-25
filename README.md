# into.py

Collect the result of a pipe expression **into** a variable with `into`.

```python

from into_py import into

def add(x, y):

    return x + y

result = into(sum, [1, 2, 3], add)

assert result == 6

```
