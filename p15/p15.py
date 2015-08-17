
limit = 20

# this works but is super long, fix it.
def lattice(r,d,tot):
    if r < limit:
        tot = lattice(r+1,d,tot)
    if d < limit:
        tot = lattice(r,d+1,tot)
    if r == limit and d == limit:
        tot += 1
    return tot

tot = 0
print(lattice(0,0,tot))
