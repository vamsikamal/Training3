lst = ['Sunday\n', 'Monday\n', 'Tuesday\n','Wednesday']
f = open('demo.txt', 'w')
f.writelines(lst)
f.close()

