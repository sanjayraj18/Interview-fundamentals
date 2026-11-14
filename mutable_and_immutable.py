
# Lists, dictionaries, sets - mutable
# Integers, strings, tuples - immutable

# list
numbers = [10, 20, 30]
numbers[0] = 99
numbers.append(40)

# tuple
numbers = (10, 20, 30)
numbers[0] = 99  # This would raise an error since tuples are immutable


# A tuple containing a list is not deeply immutable. The tuple cannot change which objects it contains, but the list inside it can change.
data = (10, [20, 30])

# Allowed: modify the existing list.
data[1].append(40)
print(data)  # (10, [20, 30, 40])

# Also allowed: change an element inside that list.
data[1][0] = 99
print(data)  # (10, [99, 30, 40])

# Not allowed: replace the list with a different list.
data[1] = [50, 60]
# TypeError: 'tuple' object does not support item assignment

