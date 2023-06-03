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

# -- Nested Lists

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])  
        
    students = sorted(students, key = lambda x: x[1])   
    second_lowest_score = sorted(list(set([x[1] for x in students])))[1] 
    
    sls_students = []
    for x in students:
        if x[1] == second_lowest_score:
            sls_students.append(x[0])

    print("\n".join(sorted(sls_students))) 

# -- Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    lst = student_marks[query_name]
    avg_lst = sum(lst) / len(lst)
    rnd_avg = format(round(avg_lst, 2), '.2f')
    print (rnd_avg)

# -- Power - Mod Power

a = int(input())
b = int(input())
m = int(input())

print(pow(a,b))
print(pow(a,b,m))

# -- Integers Come In All Sizes

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(pow(a,b) + pow(c,d))

# -- Triangle Quest

for i in range(1,int(input())):
    print(i*((10**i-1)//9))
