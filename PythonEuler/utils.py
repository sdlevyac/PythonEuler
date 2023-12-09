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

def primeSieve(limit):
    primes = [1 for i in range(limit)]
    primes[0:2] = [0,0]
    n = 2
    while n**2 < limit:
        i = 2
        while n*i < limit:
            primes[n*i] = 0
            i += 1
        n += 1
    return primes

def getPrimesUnder(limit):
    sieve = primeSieve(limit)
    return [i for i in range(limit) if sieve[i] == 1]

def product(numString):
    if "0" in numString: return 0
    answer = 1
    for num in numString:
        answer *= int(num)
    return answer

input08 = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

def product(someNums):
    ans = 1
    for num in someNums:
        ans *= num
    return ans

def pythagTriplet(target):
    for a in range(1,target - 2):
        for b in range(1, target - 1 - a):
            c = target - b - a
            if a**2 + b**2 == c**2:
                return [a, b, c]
    return [0, 0, 0]