import csv

# with open('test.csv', 'r') as file:
    # csv_reader = csv.reader(file, delimiter=';')
    # headers = next(csv_reader)
    # print(csv_reader.line_num)
    # for row in csv_reader:
    #     print(row[0])
    # print(csv_reader.line_num)


    # csv_reader = csv.DictReader(file, delimiter=';')
    # for row in csv_reader:
    #     print(row['first_name'])



#
# headers = ['first_name', 'last_name']
#
# data = [['Irakli', 'Tabatadze'], ['John', 'Doe']]
#
# with open('test2.csv', 'w') as file:
#     csv_writer = csv.writer(file)
#
#     csv_writer.writerow(headers)
#     csv_writer.writerows(data)



headers = ['first_name', 'last_name']

data = [
    {'first_name': 'John', 'last_name': 'Doe'},
    {'last_name': 'Johnson', 'first_name': 'Kate'}
]

with open('test3.csv', 'w') as file:
    dict_writer = csv.DictWriter(file, fieldnames=headers)

    dict_writer.writeheader()
    dict_writer.writerows(data)