
class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def upper(self):
        return self.username.upper()


class Product:
    def __init__(self, name:str, price:float, stock:int, user:User):
        self.name = name
        self.price = price
        self.stock = stock
        self.user = user


user1 = User("Irakli", 'Password123')

product1 = Product("Apple", 5.5, 100, user1)

# print(product1.user.username)
# print(user1.username)


print(product1.name.upper())
print(product1.user.upper())