# What is the difference between == and is? Why do we commonly use is None?

# In Python, == compares values, while is compares object identity—whether two variables refer to the exact same object.

a = [1, 2, 3]
b = [1, 2, 3]  # A separate list with the same contents
c = a          # Refers to the same list as a

print(a == b)  # True: same contents
print(a is b)  # False: different objects

print(a == c)  # True
print(a is c)  # True: same object