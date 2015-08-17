import Queue as Q

fib = [1,2]

s = 0;

while fib[1] < 4000000:
    if fib[1]%2 is 0:
        s += fib[1]
        print(fib[1])
    fib.append(sum(fib))
    fib.pop(0)




print(s)
