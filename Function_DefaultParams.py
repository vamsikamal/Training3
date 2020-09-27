def simpleinterest(p, n, r = 8):
    si = (p * n * r) / 100
    print(si)

def display(fname, lname):
    print(fname, lname)

simpleinterest(10000, 4)
simpleinterest(10000, 4, 6)

display(lname='slc', fname='python')