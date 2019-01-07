# Value returning Function

## What is Return statement?

In previous lesson, we learned that function can be reused, and automate our tedious works.  For automation, we define behaviors in the function, and we pass parameters to adjust the behaviors for each use cases.

Today, I am introducing a special statement called 'return'.
If function is the most important feature of programming language, return is the most essential feature of the function.  This is the most basic way of writing a software.

Return statement finishes the function execution and sends some data (we call it 'Return Value') back to called place.

For example,

```
def HelloString(name):
    return "Hello, " + name + "."

if __name__ == "__main__":
    hello = HelloString("Jake")
    print(hello)
```

We used variable 'hello' to store the return value from HelloString() function.  And, reused that value to the print.
Because returning value is also a value, we can even directly use the return value of HelloString("Jake") directly like this:

```
def HelloString(name):
    return "Hello, " + name + "."

if __name__ == "__main__":
    print(HelloString("Jake"))
```
