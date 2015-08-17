def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
currTri = 1
currNum = 2

while len(factors(currTri)) < 500:
    currTri += currNum
    currNum += 1
    print([currTri,len(factors(currTri))])
