def is_prime(a):
    return all(a % i for i in xrange(2, a))

primeNum = 1
currNum = 2

while primeNum < 10001:
    currNum += 1
    if is_prime(currNum):
        print(primeNum)
        primeNum += 1

print(primeNum)
print(currNum)
