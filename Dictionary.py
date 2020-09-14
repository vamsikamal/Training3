# Dict contains elements as key value pairs
dict1 = {'name':'SLC', 'course': 'Python', 'duration': 45}
print(dict1)
print(type(dict1))

print(dict1['name'])    # SLC
print(dict1.get('name')) # SLC


for k in dict1.keys():
    print(k, dict1[k])

for v in dict1.values():
    print(v)

for k,v in dict1.items():
    print(k,v)


dict1 = {'name':'SLC', 'course': 'Python', 'duration': 45}
# Adding element
dict1['trainer'] = 'Kamal'
print(dict1)

# Update element
dict1['trainer'] = 'Vamsi'
print(dict1)

# Delete
del dict1['trainer']
print(dict1)

dict1 = {'name':'SLC', 'course': 'Python', 'duration': 45, 'trainer':'vamsi', 'trainer':'kamal'}
print(dict1)

# Pop
p = dict1.pop('trainer')
print(p)
print(dict1)

pi = dict1.popitem()
print(pi)
print(type(pi))

dict1.clear()
print(dict1)  # {}

del dict1
#print(dict1)   # NameError: name 'dict1' is not defined

dict1 = {'name':'SLC', 'course': 'Python', 'duration': 45}
print(dict1['raja'])     # KeyError: 'raja'