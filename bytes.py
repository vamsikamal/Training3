# bytes type represents group of byte numbers
# 0 to 255 only
# Mutable

x = [10,20,30,40, 255]
b = bytes(x)
print(b)
print(type(b))

print(b[0])

for i in b:
    print(i)

