import string
import numpy as np

def fibList(limit):
    fibList = [1,1]
    while fibList[-1] <= limit:
        fibList.append(fibList[-1] + fibList[-2])
    return fibList

def isPrime(num):
    for i in range(2, int(np.sqrt(num))):
        if num % i == 0:
            return False
    return True

def isPalindrome(text):
    if type(text) == int:
        return str(text)[::-1] == str(text)
    else:
        return text[::-1] == text

def isDivisible(a, d):
    return a % d == 0

def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

def lcmList(numbers):
    while len(numbers) != 1:
        newnumbers = [lcm(numbers[0], numbers[1])]
        newnumbers.extend(numbers[2:])
        numbers = [n for n in newnumbers]

    print(numbers[0])
        
nums4 = [i for i in range(100,1000)]