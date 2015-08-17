def is_palindrome(inp):
    # expects and integer
    s = str(inp)
    if s == s[::-1]:
        return True
    return False

s = 0
for i in range(999,0,-1):
    for j in range(999,0,-1):
        if is_palindrome(i*j):
            if i*j > s:
                s = i*j
            print(i*j)
print(s)
