
start = 1
maxLen = 0
maxStart = 0
while start < 1000000:
    curr = start
    currLen = 0
    while curr is not 1:
        currLen += 1
        if  curr%2 is 0:
            curr /= 2
        else:
            curr = 3*curr + 1
    if currLen > maxLen:
        maxLen = currLen
        maxStart = start

    print([start, currLen])
    start += 1

print([maxStart, maxLen])
