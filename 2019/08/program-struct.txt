# Structure of Program

Usually, a computer program is composed of 3 big structures.  Input, Process, and Output.  Usually, the program collects data first (input), then process to solve the problem(process), and show the result. (output).

For example, let's make a add-2-number program:

```
if __name__ == '__main__':

    # This is input part.  We collect data from the user.
    s1 = input("Enter the first number: ")
    s2 = input("Enter the second number: ")

    # Process.
    sum = int(s1) + int(s2)

    # Output.  And, we show the result.
    print("Sum: {}".format(sum))
    
```

As we can see, this is very popular structure of a program.
Eventually, when we write functions, most functions also follow this structure.
Many times, the output of function will be "return" statement.
We will learn this more in depth, when we cover function part.

