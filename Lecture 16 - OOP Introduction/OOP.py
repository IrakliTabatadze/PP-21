# class Human:
#     eyes = 2
#     nose = 1
#     ears = 2
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def walking(self):
#         print(f"{self.first_name} can walk")
#
#     def talking(self):
#         print(f"{self.first_name} can talk")
#
#     @staticmethod
#     def running():
#         print("")
#
#     @classmethod
#     def change_eyes(cls):
#         cls.eyes = 1
#
# human1 = Human("John", "Doe")
# human1.walking()
#
# human2 = Human("Kate", "Doe")
# human2.walking()
#
# print(human1.ears)
# print(human2.ears)
#
# human2.first_name = "Irakli"
# human2.walking()
#
# human2.change_eyes()
# print(human1.eyes)
# print(human2.eyes)


############################################################
# Inheritance
############################################################
# class Animal:
#
#     legs = 4
#
#     def __init__(self, name):
#         self.name = name
#
#
# class Dog(Animal):
#
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
#
#     def bark(self):
#         print(f"{self.name} can bark")
#
#
# class Cat(Animal):
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color
#
#     def meow(self):
#         print(f"{self.name} can meow")
#
#
# cat = Cat('Garfield', 'Orange')
# dog = Dog('Fluffy', 'Pudell')
#
# print(cat.legs)
# print(dog.legs)
# dog.bark()
# cat.meow()
#
#
# dog.legs = 1
#
# print(cat.legs)
# print(dog.legs)


#######################################################
# Encapsulation
#######################################################

# class PublicEncapsulation:
#     def public_method(self):
#         print("Public Method")
#
#     def call_public_method(self):
#         self.public_method()
#
# class InheritedClass(PublicEncapsulation):
#     def __init__(self):
#         self.public_method()
#
# public_object = PublicEncapsulation()
# public_object.public_method()






# class ProtectedEncapsulation:
#     _legs = 4
#
#     def __init__(self, name):
#         self._name = name
#
#     def _protected_method(self):
#         print("Protected Method")
#
#
# protected_objects = ProtectedEncapsulation()
# protected_objects._protected_method()





# class PrivateEncapsulation:
#     def __private_method(self):
#         print("Private Method")
#
#     def call_private(self):
#         self.__private_method()
#
# class InheritedClass(PrivateEncapsulation):
#     def __init__(self):
#         self.__private_method()
#
# private_objects = PrivateEncapsulation()
# private_objects.call_private()


#######################################################
# Polymorphism
#######################################################

class Shape:
    def draw(self):
        print("Drawing")

class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")

class Circle(Shape):
    # def draw(self):
    #     print("Drawing Circle")

    def test(self):
        print("test")

shape = Shape()
rect = Rectangle()
circle = Circle()

shape.draw()
rect.draw()
circle.draw()