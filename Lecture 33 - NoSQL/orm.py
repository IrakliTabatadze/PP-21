import sqlalchemy.orm.exc

from models import session, Customers, Accounts, AccountTypes, Cities
from datetime import datetime
from sqlalchemy.orm.exc import UnmappedInstanceError

####################################################################
# Select
####################################################################
customers = session.query(Customers).all()
print(customers)

for customer in customers:
    print(customer.firstname, customer.lastname)


customers = session.query(Customers).filter(Customers.income < 20000).all()
customers = session.query(Customers).filter_by(customerid=123123).all()
print(customers)

for customer in customers:
    print(f'firstname: {customer.firstname}, lastname: {customer.lastname}, income: {customer.income}')



customers = session.query(Customers).filter(Customers.create_date>datetime(2024,8, 1)).filter(Customers.create_date>datetime(2024,10, 1)).all()
for customer in customers:
    print(f'firstname: {customer.firstname}, lastname: {customer.lastname}, create_date: {customer.create_date}')



joined_query = session.query(Customers, Cities).join(Cities, Customers.cityid==Cities.cityid).all()
joined_query = session.query(Customers, Cities).outerjoin(Cities, Customers.cityid==Cities.cityid).all()

print(joined_query)

for customer, city in joined_query:
    print(customer.firstname, customer.lastname, city.cityname)




customers = session.query(Customers.lastname,
                          Customers.firstname,
                          Cities.cityname,
                          Accounts.accountnumber,
                          Accounts.balance,
                          AccountTypes.accounttypename).join(Cities).join(Accounts).join(AccountTypes).all()

print(customers)




####################################################################
# Insert
####################################################################

customer1 = Customers('12345678', 'gvari', 'saxeli', datetime(2010, 10, 10), 6)
customer2 = Customers('12345679', 'gvari', 'saxeli', datetime(2010, 10, 10), 6)
customer3 = Customers('1234569', 'gvari', 'saxeli', datetime(2010, 10, 10), 6)

session.add(customer1)
session.commit()


customer_lst = [customer1, customer2, customer3]
session.add_all(customer_lst)
session.commit()


####################################################################
# Update
####################################################################


customer = session.query(Customers).filter_by(customerid=123456789).first()

customer.firstname = 'Irakli'
session.commit()


####################################################################
# Delete
####################################################################

try:
    customer = session.query(Customers).filter_by(customerid=123456789).first()
    session.delete(customer)

    session.commit()
except UnmappedInstanceError as e:
    print(e)

