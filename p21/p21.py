#!/usr/bin/python3.5

# gets the sum of the factors of a number
def sumOfFactors(num):
    if num is 0:
        return 0
    return sum([x for x in range(1,int(num/2)+1) if num%x is 0])

def isAmicable(num1, num2):
    return (sumOfFactors(num1) == num2 and
            sumOfFactors(num2) is num1)

amicable = []
for i in range(10000):
    j = sumOfFactors(i)
    if not j in amicable \
       and i != j \
        and i == sumOfFactors(j):
        amicable.append(i)
        amicable.append(j)
        print(amicable)

print(sum(amicable))
