# Set is group of values without duplicates
# Insertion order is not preserved and index concept is not applicable
a = {1,2,3,4,5}
b = {4,5,6,7,8}

print(a)
print(type(a))     # <class 'set'>

print(a | b)       # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))  # {1, 2, 3, 4, 5, 6, 7, 8}

print(a & b)       # {4, 5}
print(a.intersection(b))  # {4, 5}

print(a-b)               # {1, 2, 3}
print(a.difference(b))   # {1, 2, 3}

print(a^b)             # {1, 2, 3, 6, 7, 8}
print(a.symmetric_difference(b))  # {1, 2, 3, 6, 7, 8}

# Subset and superset
a = {1,2,3,4,5}
b = {2,3,4}
print(a > b)             # True
print(a.issuperset(b))   # True
print(a < b)             # False
print(a.issubset(b))     # False

# Updating
s = {1,2,3,4}
s.add(10)
s.add(10)
s.add(10)
print(s)                # {1, 2, 3, 4, 10}

s.update([10,20,30])
print(s)                # {1, 2, 3, 4, 10, 20, 30}

s.discard(10)
print(s)               # {1, 2, 3, 4, 20, 30}

s.remove(20)
print(s)               # {1, 2, 3, 4, 30}

t = s.pop()
print(t)  # 1
print(s)  # {2, 3, 4, 30}