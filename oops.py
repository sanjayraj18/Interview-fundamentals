# class
# object, instance
# Instance variable, class variable

# Encapulation -> bank example
# Inheritance -> Animal example
# Overriding -> Animal speak example
# Polymorphism -> Payment example
# Abstraction -> Coffee machine example



# Encapsulation - Encapsulation means keeping an object’s data and the operations controlling that data together.
# before eg : bank balance example
class BankAccount1:
    def __init__(self, balance):
        self.balance = balance

account = BankAccount1(1000)
account.balance = -1_000_000

# after
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # This is internal to the class. Do not change it directly unless you understand the consequences.

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount

    def get_balance(self):
        return self._balance

#Inheritance - Inheritance lets one class reuse or extend another class.
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} says woof")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} says meow")

dog = Dog("Bruno")
cat = Cat("Luna")

dog.eat()   # Bruno is eating
dog.bark()  # Bruno says woof

cat.eat()   # Luna is eating
cat.meow()  # Luna says meow


#overriding - A child class can replace inherited behavior. This is called overriding:
class Animal:
    def speak(self):
        print("Some animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")


#Composition - Composition means, building one object using another object - has-a relationship
# Composition is often more flexible than inheritance. "car has a engine"
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    def start(self):
        print(f"Starting {self.model}")
        self.engine.start()

engine = Engine()
car = Car("Honda City", engine)

car.start()


#Polymorphism - Polymorphism means different objects can respond to the same operation in their own way. eg : UPI payment
class CardPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using a card")


class UpiPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CashPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using cash")


def complete_payment(payment_method, amount):
    payment_method.pay(amount)

card = CardPayment()
upi = UpiPayment()
cash = CashPayment()

complete_payment(card, 1000)
complete_payment(upi, 1500)
complete_payment(cash, 500)

# abstraction - Abstraction means exposing the important operation while hiding unnecessary implementation details
# eg : coffee machine example
class CoffeeMachine:
    def make_coffee(self):
        self._heat_water()
        self._grind_beans()
        self._mix_ingredients()
        print("Coffee is ready")

    def _heat_water(self):
        print("Heating water")

    def _grind_beans(self):
        print("Grinding beans")

    def _mix_ingredients(self):
        print("Mixing ingredients")

machine = CoffeeMachine()
machine.make_coffee()

# Encapsulation: Keep data and the rules for changing it together.
# Abstraction: Give callers a simple interface and hide unnecessary details.