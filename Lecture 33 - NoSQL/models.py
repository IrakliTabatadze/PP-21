from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host = 'localhost'
port = 5432
database = 'postgresdb1'
user = 'postgres'
password = 'irakli24'


# Hyper Text Transfer Protocol(HTTP)
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

Base = declarative_base()

class AccountTypes(Base):
    __tablename__ = 'accounttypes'

    accounttypeid = Column('accounttypeid', Integer, primary_key=True, autoincrement=True)
    accounttypename = Column('accounttypename', String(50))

    def __init__(self, accounttypename):
        self.accounttypename = accounttypename


class Cities(Base):
    __tablename__ = 'cities'

    cityid = Column('cityid', Integer, primary_key=True, autoincrement=True)
    cityname = Column('cityname', String(30))

    def __init__(self, cityname):
        self.cityname = cityname


class Customers(Base):
    __tablename__ = 'customers'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    customerid = Column('customerid', Integer, unique=True)
    lastname = Column('lastname', String(40))
    firstname = Column('firstname', String(40))
    dateofbirth = Column('dateofbirth', Date)
    cityid = Column('cityid', Integer, ForeignKey('cities.cityid'))
    zipcode = Column('zipcode', String(4))
    street = Column('street', String(60))
    housenumber = Column('housenumber', Integer)
    income = Column('income', Float)
    create_date = Column('create_date', DateTime)
    update_date = Column('update_date', DateTime)

    def __init__(self, customerid, lastname, firstname, dateofbirth, cityid, zipcode=None, street=None, housenumber=None, income=None):
        self.customerid = customerid
        self.lastname = lastname
        self.firstname = firstname
        self.dateofbirth = dateofbirth
        self.cityid = cityid
        self.zipcode = zipcode
        self.street = street
        self.housenumber = housenumber
        self.income = income

    # def __repr__(self):
    #     return f'{self.customerid}: {self.lastname}: {self.firstname}: {self.housenumber}'


class Accounts(Base):
    __tablename__ = 'accounts'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    accountnumber = Column('accountnumber', String(100), unique=True)
    customeridnumber = Column('customeridnumber', Integer, ForeignKey('customers.customerid'))
    accounttypeid = Column('accounttypeid', Integer, ForeignKey('accounttypes.accounttypeid'))
    balance = Column('balance', Float)

    def __init__(self, accountnumber, customeridnumber, accounttypeid, balance):
        self.accountnumber = accountnumber
        self.customeridnumber = customeridnumber
        self.accounttypeid = accounttypeid
        self.balance = balance

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()