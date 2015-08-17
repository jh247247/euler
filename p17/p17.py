# 1-9
digit = [3,3,5,4,4,3,5,5,4]
# 11-19
teens = [5,5,8,8,7,7,9,9,9]
#
tens = [3,6,6,6,5,5,7,6,6]
hundred = 7
thousand = 8



curr = 1
s = 0

while curr <= 1000:
    temp = curr
    h = False
    d = False
    # last digit
    c = temp%10
    if c != 0:
        if (temp/10)%10 is 1:
            s += teens[c-1]
        else:
            s += digit[c-1]
        d = True
    temp /= 10

    # tens
    c = temp%10
    if c != 0 and c != 1:
        s += tens[c-1]
        d = True
    temp /= 10

    # hundreds
    c = temp%10
    if c != 0:
        s += digit[c-1]
        s += hundred
        if d is True:
            s += 3 # and
        h = True
    temp /= 10

    # thousand
    c = temp%10
    if c != 0:
        s += digit[c-1]
        s += thousand
        if h is True:
            s += 3
    temp /= 10

    curr += 1

print(s)
