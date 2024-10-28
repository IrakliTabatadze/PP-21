from flask import Flask, request, jsonify, Response
from models import db, Cars
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app)

host = 'localhost'
port = 5432
database = 'flask_db'
user = 'postgres'
password = 'irakli24'

app.secret_key = 'secret'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

@app.route('/', methods=['GET'])
def index():
    cars = Cars.query.all()

    cars_list = []

    for car in cars:
        car_dct = {'id': car.id, 'manufacturer': car.manufacturer, 'model': car.model, 'instock': car.instock, 'price': car.price}
        cars_list.append(car_dct)

    return jsonify(cars_list)

@app.route('/insert', methods=['POST'])
def insert_car():

    car = deserializeCar(request.json)

    db.session.add(car)
    db.session.commit()

    return Response(json.dumps({'status': 'success'}), status=201)


@app.route('/delete/<int:id>/', methods=['DELETE'])
def delete_car(id):

    car = Cars.query.get(id)

    try:
        db.session.delete(car)
        db.session.commit()

        return Response(json.dumps({'status': 'success'}), status=204)
    except Exception as e:
        return Response(json.dumps({'status': f'error {e}'}))


@app.route('/update/<int:id>', methods=['PUT'])
def update_car(id):

    car = Cars.query.get(id)

    car.manufacturer = request.json['manufacturer']
    car.model = request.json['model']
    car.instock = request.json['instock']
    car.price = request.json['price']

    db.session.commit()

    return Response(json.dumps({'status': 'success'}), status=200)


def deserializeCar(data):
    return Cars(data['manufacturer'], data['model'], data['instock'], data['price'])

if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)