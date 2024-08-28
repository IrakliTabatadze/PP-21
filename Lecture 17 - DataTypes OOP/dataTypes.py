##################################################
# Multiple Inheritance
##################################################

class Mother:
    def __init__(self, name, eye_color):
        self.name = name
        self.eye_color = eye_color

    def greet(self):
        print(f"Hello From: {self.name}")

    def bake_cookies(self):
        print(f"{self.name} is baking delicious cookies")

class Father:
    def __init__(self, name, hair_color):
        self.name = name
        self.hair_color = hair_color

    def greet(self):
        print(f"Hello From: {self.name}")

    def tell_jokes(self):
        print(f"{self.name} cracks a funny jokes")

class Child(Father, Mother):
    def __init__(self, name, eye_color, hair_color, profession, mother, father):
        Mother.__init__(self, name, eye_color)
        Father.__init__(self, name, hair_color)
        self.profession = profession
        self.mother = mother
        self.father = father

    def inherited_methods(self):
        print("Child Inherited both methods", self.mother.eye_color)


mom = Mother('Kate', 'Blue')
dad = Father('Bob', 'Black')
child = Child('John', mom.eye_color, dad.hair_color, 'Developer', mom, dad)
mom.greet()
dad.greet()
child.inherited_methods()


##################################################
# Setter & Getter
##################################################

class Person:
    def __init__(self, name, age):
        self.__name = name
        self._age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name


person = Person('John', 25)
print(person.name)
person.name = "Bob"
print(person.name)
del person.name
print(person.name)


##################################################
# Abstract Class
##################################################

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    def standard_method(self):
        print("Hello")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def print_radius(self):
        print(self.radius)


class Rectangle(Shape):
    pass

circle = Circle(10)
circle.standard_method()
rect = Rectangle()




##################################################
# Method Overload
##################################################

class Calculator:
    def add(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a + b
            print(f"Integer Result: {result}")

        elif isinstance(a, str) and isinstance(b, str):
            result = a + b
            print(f"String Result: {result}")

calc = Calculator()
calc.add(10, 20)
calc.add("10", "20")


from multipledispatch import dispatch

class Calculator:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c

    @dispatch(str, str)
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(10, 11))
print(calc.add("10", "11"))
print(calc.add(10, 10, 10))



##################################################
# Magic Methods
##################################################

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Other must be Vector")

        return Vector(self.x + other.x, self.y + other.y)

vector1 = Vector(1, 2)
vector2 = Vector(3, 4)
vector3 = vector1 + vector2
print(vector3.x, vector3.y)


class Book:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self.year)

book = Book("Rame saxeli", 1900)
print(book)


