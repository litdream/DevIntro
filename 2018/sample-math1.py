import os, sys
import random

def generate_problem(i):
    lst = [ i, ]
    for i in range(0,4):
        lst.append( random.randint(0,15))
    print('{:2d})  {:2d} + {:2d} * {:2d} - {:2d} = _____'.format(*lst))

def solution(q, a,b,c,d):
    ans = a + b * c - d
    print("{:d})  {:d} + {:d} * {:d} - {:d} = {:d}".format(q,a,b,c,d,ans))

if __name__ == "__main__":
    #for i in range(1,11):
    #    generate_problem(i)

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

