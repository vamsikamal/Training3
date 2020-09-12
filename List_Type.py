# LIST is a collection of items of different type
# LIST is mutable

# Empty
l1 = []
print(l1)          #  []
print(type(l1))    #  <class 'list'>

# List with data
l2 = [10, 20, 30, 10.5, 20.6, 'SLC', True, False]

# Indexing, reverse indexing and slicing works same as string
print(l2[2])    # 30
print(l2[-1])   # False
print(l2[2:5])  # [30, 10.5, 20.6]
print(l2[::-1]) # [False, True, 'SLC', 20.6, 10.5, 30, 20, 10]
print(l2[::2])  # [10, 30, 20.6, True]

# Nested List
l3 = [100, 200, l2]
l4 = [10, 20, [100, 200, 300]]
print(l4[2])   # [100, 200, 300]
print(l4[2][2])  # 300
print(l3[2][5])  # SLC

# Add element to list
l1 = [1,2,3,4]
l1.append(10)
print(l1)       # [1, 2, 3, 4, 10]

l1 = [1,2,3,4]
l1.extend([10,20,30])
print(l1)       # [1, 2, 3, 4, 10, 20, 30]

l1 = [1,2,3,4]
l1.append([10,20,30])
print(l1)       # [1, 2, 3, 4, [10, 20, 30]]

l1 = [1,2,3,4]
l1.insert(1, 10)
print(l1)      # [1, 10, 2, 3, 4]

# Update element
l1 = [1,2,3,4]
l1[2] = 30
print(l1)   # [1, 2, 30, 4]

l1[1:3] = [111,222]
print(l1)   # [1, 111, 222, 4]

# Remove element for list
l1 = [10,20,30,40]
del l1[2]
print(l1)   # [10, 20, 40]

l1 = [10,20,30,40,50,60]
del l1[2:4]
print(l1)  # [10, 20, 50, 60]

l1 = [10,20,30,40,50,60]
t = l1.pop()
print(l1)   #  [10, 20, 30, 40, 50]
print(t)    # 60

l1 = [10,20,30,40,50,60]
t = l1.pop(2)
print(l1)   #  [10, 20, 40, 50, 60]
print(t)    # 30

# l1 = []
# t = l1.pop()   # IndexError: pop from empty list

l1 = [1,2,3,4]
l1.clear()  # Removes elements
print(l1)  # []

l1 = [1,2,3,4]
del l1     # Deletes entire object
# print(l1)

l1 = [10,20,10,30,40,10]
print(l1.index(40))   # 4 if element exists then gives index otherwise it will give error
print(l1.count(10))   # 3

l1.sort()
print(l1)  # [10, 10, 10, 20, 30, 40]

l1.reverse()
print(l1)  # [40, 30, 20, 10, 10, 10]


l1 = [10,20,10,30,40,10]
l2 = sorted(l1)
print(l1)  # [10, 20, 10, 30, 40, 10]
print(l2)  # [10, 10, 10, 20, 30, 40]

l1 = [10,20,10,30,40,10]
l2 = reversed(l1)
print(l1)

# Functions
l1 = [10,20,10,30,40,10]
print(max(l1))   # 40
print(min(l1))   # 10
print(sum(l1))   # 120
print(any(l1))   # True
print(all(l1))   # True