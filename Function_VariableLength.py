def bill(*price):
    # print(type(price))
    sum = 0
    for i in price:
        sum = sum + i

    print(sum)


bill(10,20)
bill(10,20,30,40,50)