# Compare lists, tuples, sets, and dictionaries. When would you choose each?

# | Type     | Ordered?             | Duplicates? | Mutable? | Access   
# | `list`   | Yes                  | Yes         | Yes      | By index 
# | `tuple`  | Yes                  | Yes         | No       | By index 
# | `set`    | No guaranteed order  | No          | Yes      | Membership, not index 
# | `dict`   | Yes, insertion order | Keys: No    | Yes      | By key 

# List - Choose a list when order matters and you may need to add, remove, or replace elements.
# Tuple - choose a tuple when the collection’s structure should not change.
# Set - choose a set when uniqueness or fast membership checking matters. Sets do not support indexing. Sets are especially useful for removing duplicates:
# Dictionary - choose a dictionary when you need to associate keys with values and access them by key.