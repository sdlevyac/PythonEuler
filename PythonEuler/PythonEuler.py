import numpy as np
from utils import *

def problem01():
    return sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])

def problem02():
    return sum(f for f in fibList(4000000) if f % 2 == 0)

def problem03():
    return max([i for i in range(1, int(np.sqrt(600851475143)) + 1) if 600851475143 % i == 0 and isPrime(i)])

print(problem01())
print(problem02())
print(problem03())