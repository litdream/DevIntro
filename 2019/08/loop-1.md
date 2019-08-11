# Loop

What is loop?  In python, loop is a block statement using `for` or `while`.

When we have to repeat a certain logic, we can use loop to make repeating logic easy.
However, when writing a loop, discovering the pattern is the key.  Once the pattern is discovered, the logic has to be adjusted to be fit into loop.
There are different forms of loop.  I think Examples will make this clear.

## Repeat N times, and built-in function range()

If we know how many times to be repeated, we can use for-loop and range() function.
range() function is a built-in function.  It gives a range of integers in turn.
Let's see a simple for-loop and range example.

```
>>> for i in range(0,10):
...   print(i)
...
0
1
2
3
4
5
6
7
8
9
```

We printed numbers from 0 to 9.  What happened here is, range(0, 10) will prepare numbers from 0 to 9 (excluding 10).  And, print() function is executed in turn inside for-loop.  This range repeated 10 times, including 0, but excluding 10.  In other words, range(0,10) is the same as range(0).

```
>>> for i in range(10):
...   print(i)
...
0
1
2
3
4
5
6
7
8
9
```

If we have to change this to the way we human count (starting from 1 to 10), it will be somewhat strange:

```
>>> for i in range(1,11):
...   print(i)
...
1
2
3
4
5
6
7
8
9
10
```

