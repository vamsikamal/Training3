# Tuple is collection of items of different type
# Tuple is immutable

# Tuple
tup = (12, 30, 'Hi', 10.56)
print(tup)
print(type(tup))

# Packing
t = 10,20,30,40
print(t)
print(type(t))

# Unpacking
a,b,c,d = t
print(a)
print(b)
print(c)
print(d)

# Read data from tuple is similar to list only
print(t[0])
print(t[-1])
print(t[1:3])
print(t[1:4:2])

# Add, Delete, Update operations are not supported in tuples
