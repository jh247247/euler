from math import sqrt

def is_square(a):
    return int(sqrt(a) + 0.5)**2 == a




limit = 1000
i = 1
j = 1
pyth = True
while i < limit and pyth is True:
    j = i
    i += 1
    while j < limit and pyth is True:
        j += 1
        if is_square(i**2+j**2):
            #print([i,j,int(sqrt(i**2+j**2)),int(i+j+sqrt(i**2+j**2))])
            if int(i+j+sqrt(i**2+j**2)) == 1000:
                print([i,j,sqrt(i**2+j**2)])
                print([i*j*sqrt(i**2+j**2)])
