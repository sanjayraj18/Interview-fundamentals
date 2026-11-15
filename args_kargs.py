# *args lets a function accept any number of additional positional arguments.
# **kwargs lets a function accept any number of additional keyword arguments.

def example(required, *args, **kwargs):
    print("Required:", required)
    print("Extra positional:", args)
    print("Extra keywords:", kwargs)

example(
    "first",
    10,
    20,
    name="Sanjay",
    active=True,
)

# output:
# Required: first
# Extra positional: (10, 20)
# Extra keywords: {'name': 'Sanjay', 'active': True}


# next topic 
# return → produce the final result and finish
# yield  → produce one value, pause, and continue later