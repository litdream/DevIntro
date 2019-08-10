# IDLE

## What is IDLE?

This is a python interactive shell.  Then, what is an interactive shell?
An interactive shell is running a python program, line-by-line manually.
The opposite of an "Interactive Python" is, code written on Visual Studio Code.
Once our "main.py" is written, this code runs all together inside of a python interpreter.

Interactive shell, however, we have a python interpreter up front.
We give command to run, line by line, and we get feed-back from the python interpreter.
This is a great way of:
 - Test
 - And, Learning a new stuff.
 
## Opening IDLE

### Windows Menu.

Open windows menu -> Find a 3.x version of Python -> IDLE

### Windows Search

Next to Windows Menu, type "IDLE" in the Search box.  Any 3.x IDLE will work.


## Useful IDLE commands.

### dir()

dir() shows summary of variable/methods of an object.  An Example:

```
>>> name = "JAKE"
>>> dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

As you see, variable _name_ is a string "JAKE".
and, when we ask to the shell, "dir(name)", the shell will give what I can access inside of string object(name).

For example, we see _lower_ function in the name object:

```
>>> name
'JAKE'
>>> name.lower()
'jake'

```
This made name string to lower case.

Another example.  We briefly handled python list.  And, list provides different methods:
```
>>> lst = [1,2,3]
>>> dir(lst)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

For example, we can reverse the list:
```
>>> lst
[1, 2, 3]
>>> lst.reverse()
>>> lst
[3, 2, 1]
```

### help()

help() gives documentation of a given object.
For example, if we want to know details of methods, we can use:

```
>>> help(lst)
Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.

....

 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 

```

This documentation explains details of each method, listed by dir(lst).

#### Some are not available (such as string/str object)

The first thing we can try is always object variable name.  This mostly works except for string object.  For example, we have `name` and `lst` variable to make "JAKE" and `[1, 2, 3]` as its content.  We saw that `help(lst)` gives us a good documentation.  But, if we try `help(name)`:

```
>>> help(name)
No Python documentation found for 'JAKE'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.


```

This is a special case for string object (name).  
In this case, shell suggests to use `help(str)` instead of `help(name)`.  Then, we can get documentations.


```
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 
...

 |  Static methods defined here:
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.


```

