# A closure is a function that remembers values from the place where it was created.
# A decorator is a function that wraps another function to add behavior without changing that function’s code.

def make_multiplier(multiplier):
    def multiply(number):
        return number * multiplier

    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))  # 20
print(triple(10))  # 30

# conceptually
# double ──> multiply()
#              remembers multiplier = 2

# triple ──> multiply()
#              remembers multiplier = 3


# practical use case
# Suppose different products have different tax rates:
def create_price_calculator(tax_rate):
    def calculate(price):
        tax = price * tax_rate
        return price + tax

    return calculate

india_calculator = create_price_calculator(0.18)
lower_tax_calculator = create_price_calculator(0.05)

print(india_calculator(1000))     # 1180.0
print(lower_tax_calculator(1000)) # 1050.0


# decorator
# problem statement : Run some extra code before and after a function without rewriting that extra code inside every function.
def log_call1(function):
    def wrapper():
        print(f"Calling {function.__name__}")

        result = function()

        print(f"Finished {function.__name__}")
        return result

    return wrapper


def log_call(function):
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Finished {function.__name__}")
        return result

    return wrapper

@log_call
def add(a, b):
    return a + b


answer = add(10, 20)
print(answer)
