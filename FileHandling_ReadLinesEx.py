f = open('demo.txt','r')
lines = f.readlines()
#print(type(lines))
#print(lines)
for line in lines:
    print(line, end='')