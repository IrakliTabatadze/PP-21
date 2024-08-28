
class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"

class House:
    def __init__(self, ID: int, price: int, owner: Person, status='For Sale'):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status

    def sell_house(self, buyer: Person, loan_amount=0):
        if loan_amount > 0:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = 'SOLD By Loan'
            self.owner.loan += loan_amount
            print(f"House Sold By Loan, Owner is {self.owner}")

        else:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = 'SOLD'
            print(f"Person Who Bought This House: {self.owner}. It's status is: {self.status}")



person1 = Person('John')
person2 = Person('Kate', 50000)

house = House(123456789, 100000, person1)
house.sell_house(person2, 50000)



#################################################################
# Decorators
#################################################################

def transaction_decorator(func):
    def wrapper(*args, **kwargs):
        print(args)
        x = args[0]
        y = args[1]
        if x - y - 1 >= 0:
            return func(x, y)
        else:
            return "Not Enough Money"

    return wrapper


@transaction_decorator
def transaction(deposit, amount):
    return deposit - amount

print(transaction(1000, 1000))



#################################################################
# Functors
#################################################################

class Functor:
    def __call__(self, name, *args, **kwargs):
        print(args, kwargs)

functor = Functor()
functor()



#################################################################
# Descriptors
#################################################################


class Descriptor:

    def __get__(self, instance, owner):
        print("Getting value")
        return instance.name

    def __set__(self, instance, value):
        print(f"Setting Value: {value}")
        instance.name = value

    def __delete__(self, instance):
        print("Deleting Attribute")
        del instance.name


class TestClass:
    def __init__(self, name):
        self.name = name

    descriptor = Descriptor()


obj = TestClass("John")
value = obj.descriptor
print(obj.descriptor)
obj.descriptor = "Kate"
print(obj.descriptor)
del obj.descriptor
print(obj.descriptor)



#################################################################
# __new__
#################################################################


class TestClass:
    def __new__(cls, *args, **kwargs):
        print("__new__ constructor")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        self.name = name
        print("__init__ constructor")

obj = TestClass("John")


#################################################################
# Metaclasses
#################################################################

class Car(type):
    def __new__(cls, name, bases, dct):
        instance = super().__new__(cls, name, bases, dct)
        return instance


class ElectricCar(metaclass=Car):
    def __init__(self, name):
        self.name = name

    def print_name(self):
        return self.name

print(type(Car))
print(type(ElectricCar))