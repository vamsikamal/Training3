# filter(function, collection)

# Without Lambda expression
def IsEven(n):
    if n%2 == 0:
        return True
    else:
        return False

list1 = [1,2,3,4,5,6,7,90]
list2 = list(filter(IsEven, list1))
print(list2)
filter

# With Lambda expression
list3 = [1,2,3,4,5,6,7,90]
list4 = list(filter(lambda x : x%2 == 0, list3))
print(list4)


