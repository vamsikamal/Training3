# Map function without lambda expression
def doublethenumber(n):
    return 2*n

list1 = [1,2,3,4,5]
list2 = list(map(doublethenumber, list1))
print(list2)


# Map function using lambda expression
list3 = [1,2,3,4,5]
list4 = list(map(lambda n: n*2, list3))
print(list4)