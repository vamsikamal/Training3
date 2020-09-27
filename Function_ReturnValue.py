def display():
    #
    return 'Hello'

def add(num1, num2):
    return num1 + num2

def calc(num1, num2):
    sum = num1+num2
    diff = num1 - num2
    prod = num1 * num2
    return sum, diff, prod

a = display()
print(a)

sum = add(10,20)
print(sum)

s, d, p = calc(20,10)
print(s, d, p)
