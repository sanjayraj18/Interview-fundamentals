def add_item1(item, items=[]):
    print(id(items))
    items.append(item)
    return items

add_item1("apple")
# ['apple']
add_item1("banana")
# ['apple', 'banana']
add_item1("orange")
# ['apple', 'banana', 'orange']


# the standard fix:
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items

print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['banana']
print(add_item("orange"))  # ['orange']