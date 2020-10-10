try:
    n = int(input('Enter a number: '))
    a = 10 / n
    print(n)

except ValueError as msg:
    print('Error occured', msg)
except ZeroDivisionError as msg:
    print(msg)
except:
    print('Except class')
finally:
    print('finally block executed')