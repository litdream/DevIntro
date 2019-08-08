# Function, part 1

Function is made to reuse the same logic in multiple places.
In a very simplistic way, you can consider that a "function" will replace "the logic" part.

## Simple usage 1.

We have math home, and let's write a program to solve the homework.

```
 1)   9 +  1 *  5 -  9 = _____
 2)   7 +  8 *  0 - 11 = _____
 3)  12 +  0 *  1 - 13 = _____
 4)  15 +  0 * 13 -  8 = _____
 5)   3 + 12 *  3 - 14 = _____
 6)   3 + 15 *  5 -  8 = _____
 7)   1 +  6 *  6 -  5 = _____
 8)  12 +  7 *  4 -  9 = _____
 9)   9 +  0 * 10 -  1 = _____
10)   1 +  8 *  8 -  8 = _____
```

We can write a redundant code like this:

```
if __name__ == "__main__":
    # Q1.
    ans = 9 + 1 * 5 - 9
    print("9 + 1 * 5 - 9 = ", ans)

    # Q2.
    ans = 7 + 8 * 0 - 11
    print("7 + 8 * 0 - 11 = ", ans)

    # Q3.
    ans = 12 + 0 * 1 - 13
    print("12 + 0 * 1 - 13 = ", ans)

    # Q4.
    #   TODO: Finish the rest of th code.
    #   ...
```

But, this makes lots of labor.  We are getting tired using computer, rather than getting help from the computer.
There must be a simpler way to describe our problem.  There are two patterns we can discover.

1. Our `ans` calculation is repeated in `print()` statement.  The data is used differently (one for calculating number, the other for printing), but same data are used.
2. And, how we describe in Q1 is the exactly the same way to describe in Q2, except the data are used.  And, this data is consistently used in the same question.

The same actions but, producing different outcome based on different data can be grouped as a function.
Remember your math class, such that  `f(x) = x * 3`.  When x is 3, f(3) becomes 9.  We call x, a parameter.
If we make parameters for each question, and describe the pattern as a reusable code, that is called _FUNCTION_.

Let me rewrite that code.

```
def solution(q, a,b,c,d):
    ans = a + b * c - d
    print(q, ")  ", a, " + ", b, " * ", c, " - ", d, " = ", ans)

if __name__ == "__main__":
    solution(1, 9,1,5,9)
    solution(2, 7,8,0,11)
    solution(3, 12,0,1,13)
    solution(4, 15,0,13,8)
    solution(5, 3,12,3,14)
    solution(6, 3,15,5,8)
    solution(7, 1,6,6,5)
    solution(8, 12,7,4,9)
    solution(9, 9,0,10,1)
    solution(10, 1,8,8,8)

```

The function "solution" has 5 parameters, explaining in order:
- q : question number
- a : first term of the math expression.
- b : second
- c : third
- d : fourth

This is similar to how you use "Block" in Scratch.
Python will provide different ways to use Functions.  Stay tuned.
