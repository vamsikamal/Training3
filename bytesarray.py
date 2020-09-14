# bytes type represents group of byte numbers
# 0 to 255 only
# immutable
x = [10,20,30,40]
b = bytearray(x)
print(b)
print(type(b))

print(b[2])
b[2] = 222

for i in b:
    print(i)