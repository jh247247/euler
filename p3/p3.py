
def is_prime(a):
    return all(a % i for i in xrange(2, a))

inp = 600851475143

lprime = 0
curr = 1

while inp > 1:
    if inp%curr == 0 and is_prime(curr):
        inp = inp/curr
        lprime = curr
        print([lprime,inp])
    curr += 1
