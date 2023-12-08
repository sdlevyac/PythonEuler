import numpy as np
from utils import *

def problem01():
    return sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])

def problem02():
    return sum(f for f in fibList(4000000) if f % 2 == 0)

def problem03():
    return max([i for i in range(1, int(np.sqrt(600851475143)) + 1) if 600851475143 % i == 0 and isPrime(i)])

def problem04():
    return max([product for product in [nums4[i % len(nums4)] * nums4[int(i / len(nums4))] for i in range(len(nums4)**2)] if isPalindrome(product)])

def problem05():
    return lcmList(list(range(1,21)))

print(problem05())