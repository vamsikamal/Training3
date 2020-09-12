str = "WELCOME"
print(str)              # WELCOME
print(type(str))        # <class 'str'>
print(len(str))         # 7

# Indexing
print(str[0])           # W
print(str[-1])          # E
print(str[3])           # C

# Slicing
print(str[1:4])         # ELC
print(str[-6:-2])       # ELCO
print(str[:4])          # WELC
print(str[1:])          # ELCOME
print(str[:])           # WELCOME

# Slicing with Jump
print(str[1:6:2])       # ECM
print(str[1:6:3])       # EO
print(str[::2])         # WLOE
print(str[::-1])        # EMOCLEW

# Functions
s = "  SLC   "
print(s.lstrip())       # Unwanted space in the left side will be removed
print(s.rstrip())       # Unwanted space in the right side will be removed
print(s.strip())        # Trims the string

# Replace
s1 = "Welcome to Java"
s2 = s1.replace("Java","Python")
print(s2)               # Welcome to Python

# Case
print(s1.upper())       # WELCOME TO JAVA
print(s1.lower())       # welcome to java
print(s1.title())       # Welcome To Java
# print(s1.lower().replace("w",s1[0].upper()))

print(s1.find("Java"))    # 11
print(s1.index("Java"))   # 11

print(s1.find("Java1"))    # 11
#print(s1.index("Java1"))   # Error
print(s1.count("e"))        # 2
s4 = ''.join(reversed(s1))
print(reversed(s1))          # <reversed object at 0x00E5C2F8>
print(s4)                   # avaJ ot emocleW