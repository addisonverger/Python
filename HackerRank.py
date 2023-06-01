# Challenges provided by HackerRank: https://www.hackerrank.com/
# All answers written in Python3

# --Say "Hello, World!" With Python

print("Hello, World!")

# --Python If-Else

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

# --Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a + b)
print(a - b)
print(a * b)

# --Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a//b)
print(a/b)
