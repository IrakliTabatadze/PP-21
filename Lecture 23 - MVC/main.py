from flask import Flask, Response, render_template
from models import Product, User
from faker import Faker
from random import randint

fake = Faker()

user = User('John')

product1 = Product(fake.name(), randint(10, 100), randint(0,20), fake.text(), user)
product2 = Product(fake.name(), randint(10, 100), randint(0,20), fake.text(), user)
product3 = Product(fake.name(), randint(10, 100), randint(0,20), fake.text(), user)
product4 = Product(fake.name(), randint(10, 100), randint(0,20), fake.text(), user)
product5 = Product(fake.name(), randint(10, 100), randint(0,20), fake.text(), user)

app = Flask(__name__)

@app.route('/')
def index():
    # return Response("<h1>Hello World</h1>")
    return render_template('index.html')

@app.route('/shop')
def shop():
    print(product1)
    # return render_template('shop.html', product=product1)
    return render_template('shop.html', products=[product1, product2, product3, product4, product5])


if __name__ == '__main__':
    app.run(debug=True)

