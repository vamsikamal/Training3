num = int(input("Enter a number: "))
count = 0
for i in range(2,num):
    if num % i == 0:
        count = count + 1

if count == 0:
    print("Prime number")
else:
    print("Not a prime number")



