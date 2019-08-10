# Python List

## What is a LIST?

In Python, each variable only holds one value.
For example,

```
>>> num1 = 1
>>> num1
1
>>> num1 = 3
>>> num1
3

```

## Accessing an item in the list.

We can't store value '1' and '3' into the variable `num1` at the same time.
When the second value, 3, is stored to num1, it's overwriting previous value, 1.
List helps to store similar values together, like this:

```
>>> lst = [ 1, 3 ]
>>> lst
[1, 3]
>>> lst[0]
1
>>> lst[1]
3
```

lst variable holds a list `[ 1, 3 ]`.  And, we could store 1 and 3 into the same container, we call this a LIST.  Also, we can access its element individually by using each index.  For example, lst[0] will access the first element of lst, 1.  And, lst[1] will access the second element of lst, 3.

## Length of the list:

There is a function called, len().  We can find out the length of a list.
```
>>> a = [ 1,2 ]
>>> len(a)
2
>>> b = [ 3,4,5 ]
>>> len(b)
3
```

## Add/Remove elements in the list

lst can be modified.
```
>>> lst
[1, 3]
>>> lst.append(5)
>>> lst
[1, 3, 5]
```
`lst.append(5)` added a new element, 5, at the end of the previous list `[1, 3]`.  This made the final shape of `[1, 3, 5]`.

We can remove this values out from the back.
```
>>> lst
[1, 3, 5]
>>> lst.pop()
5
>>> lst
[1, 3]
>>> lst.pop()
3
>>> lst
[1]
```
As seen in this example, each pop() removed the last item, and reduced the list.

## Empty list?

What happens, if we remove the last object in the list?
```
>>> lst
[1]
>>> lst.pop()
1
>>> lst
[]
>>> len(lst)
0
```

`[]` denotes an empty list.  This is an important form, because many times, we want to initialize a list in an empty state.  We can also initialize an empty list like this:

```
>>> empty1 = []
>>> empty1
[]
>>> empty2 = list()
>>> empty2
[]
```

## Reverse/Sort a list.

List has many useful methods in it.  Here let's talk about very useful functions.
As name indicates,  reverse() will make the list backward ordered.  sort() will sort the list from small to large.

```
>>> lst = [ 2,7,7,4,3,12,8,5,3,]
>>> lst
[2, 7, 7, 4, 3, 12, 8, 5, 3]
>>> lst.reverse()
>>> lst
[3, 5, 8, 12, 3, 4, 7, 7, 2]
>>> lst.sort()
>>> lst
[2, 3, 3, 4, 5, 7, 7, 8, 12]

```
