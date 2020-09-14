# Frozenset is similar to set only, but it is immutable
s = {1,2,3,4}
fs = frozenset(s)
print(fs)
print(type(fs))

for i in fs:
    print(i)

