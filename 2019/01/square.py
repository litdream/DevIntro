import os
import sys

def square(n):
    return n*n

if __name__ == "__main__":
    limit = 10

    for i in range(-limit, limit+1):
        print('*' * square(i), i)
