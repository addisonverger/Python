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

# -- Incorrect Regex

import re

T = int(input())

for _ in range(T):
    string = input()
    try:
        re.compile(string)
        print(True)
    except re.error:
        print(False)

# -- String Split and Join

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# -- What's Your Name?

def print_full_name(first_name, last_name):
    name_string = "Hello " + first_name + " " + last_name + "! You just delved into python."
    print(name_string) 

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# -- Mutations

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# -- Find a string

def count_substring(string, sub_string):
    count = 0
    start = 0
    while start < len(string):
        index = string.find(sub_string,start)
        if index == -1:
            break
        count += 1
        start = index + 1

    return count
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# -- String Validators

if __name__ == '__main__':
    s = input()
    
    if any(x.isalnum() for x in s):
        print("True")
    else:
        print("False")
    
    if any(x.isalpha() for x in s):
        print("True")
    else:
        print("False")
    
    if any(x.isdigit() for x in s):
        print("True")
    else:
        print("False")
    
    if any(x.islower() for x in s):
        print("True")
    else:
        print("False")
    
    if any(x.isupper() for x in s):
        print("True")
    else:
        print("False")  

# -- Text Alignment

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
