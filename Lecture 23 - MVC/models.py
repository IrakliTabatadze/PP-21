

class User:
    def __init__(self, name):
        self.name = name

class Product:
    def __init__(self, name, price, quantity, description, owner):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.owner = owner

    def __str__(self):
        return self.name