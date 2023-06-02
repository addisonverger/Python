# Challenges provided by HackerRank: https://www.hackerrank.com/
# All answers written in Python3

# -- Say "Hello, World!" With Python

print("Hello, World!")

# -- Python If-Else

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:
        print('Weird')
    else:
        if n >=2 and n <= 5:
            print('Not Weird')
        elif n >= 6 and n <= 20:
            print('Weird')
        else:
            print('Not Weird')

# -- Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a + b)
    print(a - b)
    print(a * b)

# -- Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)

# -- Loops

if __name__ == '__main__':
    n = int(input())

    i = 0
    while i < n:
        print(pow(i, 2))
        i += 1

# -- Write a function

def is_leap(year):
    leap = False
    
    if(year % 400 == 0):
        leap = True
    elif(year % 4 == 0 and year % 100 != 0):
        leap = True
    
    return leap

    year = int(input())
    print(is_leap(year))

# -- Print Function

if __name__ == '__main__':
    n = int(input())

    i = 1
    list = []
    while i <= n:
        list.append(i)
        i += 1

    str_list = [str(x) for x in list]

    print("".join(str_list))

# -- List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    coords=[]

    for i in range(x + 1): 
        for j in range(y + 1): 
            for k in range(z + 1): 
                if ((i + j + k) != n):
                    coords.append([i,j,k])

    print(coords)

 # -- Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr2 = list(set(arr))
    arr2.sort()
    print(arr2[-2])
