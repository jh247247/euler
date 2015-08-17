# Find the sum of the digits in the number 100!

# hopefully I don't have to use the bignum libs...

def sumNumDigits(num):
    return sum([int(i) for i in str(num)])

def factorial(order):
    ret = 1;
    for i in range(1,order+1):
        ret *= i
    return ret

print(sumNumDigits(factorial(100)))
