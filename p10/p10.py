import math
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

primeSum = 2
currNum = 2

while currNum < 2000000:
    currNum += 1
    if is_prime(currNum):
        print(currNum)
        primeSum += currNum

print(primeSum)
