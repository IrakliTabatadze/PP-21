import psycopg2

host = 'localhost' # 127.0.0.1
port = 5432
database = 'postgresdb1'
user = 'postgres'
password = 'irakli24'


connection = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)
print('Connection established')

cursor = connection.cursor()

# query = '''select customerid, lastname, firstname, cityname, accountnumber, accounttypename, balance from customers
#     left join cities on customers.cityid = cities.cityid
#     inner join accounts on customers.customerid = accounts.customeridnumber
#     left join accounttypes on accounts.accounttypeid = accounttypes.accounttypeid
#     group by customerid, lastname, firstname, cityname, accountnumber, accounttypename, balance'''

# query = 'SELECT * FROM customers WHERE customerid=123123'
#
# cursor.execute(query)
#
# print(cursor.fetchone())
# print(cursor.fetchall())


query = "insert into cities(cityname) values('New York')"

cursor.execute(query)

connection.commit()

connection.close()