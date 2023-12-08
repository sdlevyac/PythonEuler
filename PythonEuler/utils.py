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
