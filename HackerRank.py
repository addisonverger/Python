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

# -- Text Wrap

import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    w_string = wrapper.fill(text=string)
    return(w_string)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# -- Designer Door Mat

N, M = map(int, input().split())
d = '.|.'
w = 'WELCOME'

#Top Pattern
for i in range(1,((N-1)//2)+1):
    print((d*(2*i-1)).center(M, '-'))

#Welcome
print(w.center(M, '-'))

#Bottom Pattern
for i in range(((N-1)//2), 0, -1):
    print((d*(2*i-1)).center(M, '-'))

# -- String Formatting

def print_formatted(number):
    lngth = len(bin(number)[2:])
    for i in range (1, number + 1):
        print(str(i).rjust(lngth, ' '), oct(i)[2:].rjust(lngth, ' '), hex(i)[2:].rjust(lngth, ' ').upper(), bin(i)[2:].rjust(lngth, ' '))
                
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# -- Lists

if __name__ == '__main__':
    N = int(input())
    l = []
    
    for i in range(N):
        cmd, *args = input().split()
        args = [int(x) for x in args]
        if cmd == 'insert':
            l.insert(args[0],args[1])
        elif cmd == 'print':
            print(l)
        elif cmd == 'remove':
            l.remove(args[0])
        elif cmd == 'append':
            l.append(args[0])
        elif cmd == 'sort':
            l.sort()
        elif cmd == 'pop':
            l.pop()
        elif cmd == 'reverse':
            l.reverse()

# -- Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    t = tuple(integer_list)
    print(hash(t))

# -- Sum and Prod

import numpy

N, M = map(int, input().split())
my_array = []

for i in range(N):
    l = list(map(int, input().split()))
    my_array.append(l)

arr_sum = numpy.sum(my_array, axis = 0)
print(numpy.prod(arr_sum))

# -- Min and Max

import numpy

N, M = map(int, input().split())
my_array = []

for i in range(N):
    l = list(map(int, input().split()))
    my_array.append(l)
    
arr_min = numpy.min(my_array, axis = 1)
print(numpy.max(arr_min))

# -- Mean, Var, and Std

import numpy

N, M = map(int, input().split())
my_array = []

for i in range(N):
    l = list(map(int, input().split()))
    my_array.append(l)
    
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(round(numpy.std(my_array, axis = None), 11))

# -- Dot and Cross

import numpy

N = int(input())
A = []
B = []

for i in range(N):
    l = list(map(int, input().split()))
    A.append(l)

for i in range(N):
    l = list(map(int, input().split()))
    B.append(l)

print(numpy.dot(A, B))

# -- Inner and Outer

import numpy

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(numpy.inner(A, B))
print(numpy.outer(A, B))

# -- Polynomials

import numpy

P = list(map(float, input().split()))
x = int(input())

print(numpy.polyval(P, x))

# -- Linear Algebra

import numpy

N = int(input())
A = []

for i in range(N):
    l = list(map(float, input().split()))
    A.append(l)
    
print(round(numpy.linalg.det(A), 2))

# -- sWAP cASE

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# -- Capitalize!

#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    names = s.split(' ')
    capitalized_names = [name.capitalize() for name in names]
    result = ' '.join(capitalized_names)
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# -- itertools.product()

import itertools

A = list(map(int, input().split()))
B = list(map(int, input().split()))

l = list(itertools.product(A, B))
print(" ".join(map(str, l)))

# -- itertools.permutations()

from itertools import permutations

S, k = input().split()
S = [*S]
k = int(k)

l = sorted(list(permutations(S, k)))

for i in l:
    print("".join(i))

# -- itertools.combinations()

from itertools import combinations

S, k = input().split()
k = int(k)
S = sorted([*S])

arr = []

for i in range(1, k+1):
    l = list(combinations(S, i))
    arr += l

for i in arr:
   print("".join(i))

# -- itertools.combinations_with_replacement()

from itertools import combinations_with_replacement

S, k = input().split()
S = sorted([*S])
k = int(k)

arr = list(combinations_with_replacement(S,k))

for i in arr:
    print("".join(i))

# -- Set .add()

N = int(input())
S = set()

for x in range(N) :
    c = input()
    S.add(c)

print(len(S))

# -- Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    cmd, *args = input().split()
    args = [int(x) for x in args]
    if cmd == 'remove':
        s.remove(args[0])
    elif cmd == 'discard':
        s.discard(args[0])
    elif cmd == 'pop':
        s.pop()
        
print(sum(s))

# -- Set .union() Operation

n = int(input())
N = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))

N = N.union(B)
print(len(N))

# -- Set .intersection() Operation

n = int(input())
N = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))

N = N.intersection(B)
print(len(N))

# -- Set .difference() Operation

n = int(input())
N = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))

N = N.difference(B)
print(len(N))
