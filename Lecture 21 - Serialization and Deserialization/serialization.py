###############################################
# Serialization
###############################################
import json

# import json

# data = [
#         {
#         'electronics': {
#             'laptops': {
#                 'apple': {
#                     1001: {'model': 'Macbook Pro', 'price': 6000},
#                     1002: {'model': 'Macbook Air', 'price': 4000}
#                 },
#                 'HP': {
#                     2001: {'model': 'Pavillion', 'price': 2000},
#                     2002: {'model': 'G250', 'price': 2000}
#                 }
#             },
#             'phones': {
#                 'samsung': {
#                     3001: {'model': "S24 Ultra", 'price': 2000}
#                 }
#             }
#         },
#         'clothes': {
#             'shirts': {
#                 'Nike': {
#                     4001: {'ragac key': 'ragac value'}
#                 }
#             }
#         }
#     },
# {
#         'electronics': {
#             'laptops': {
#                 'apple': {
#                     1001: {'model': 'Macbook Pro', 'price': 6000},
#                     1002: {'model': 'Macbook Air', 'price': 4000}
#                 },
#                 'HP': {
#                     2001: {'model': 'Pavillion', 'price': 2000},
#                     2002: {'model': 'G250', 'price': 2000}
#                 }
#             },
#             'phones': {
#                 'samsung': {
#                     3001: {'model': "S24 Ultra", 'price': 2000}
#                 }
#             }
#         },
#         'clothes': {
#             'shirts': {
#                 'Nike': {
#                     4001: {'ragac key': 'ragac value'}
#                 }
#             }
#         }
#     },
# {
#         'electronics': {
#             'laptops': {
#                 'apple': {
#                     1001: {'model': 'Macbook Pro', 'price': 6000},
#                     1002: {'model': 'Macbook Air', 'price': 4000}
#                 },
#                 'HP': {
#                     2001: {'model': 'Pavillion', 'price': 2000},
#                     2002: {'model': 'G250', 'price': 2000}
#                 }
#             },
#             'phones': {
#                 'samsung': {
#                     3001: {'model': "S24 Ultra", 'price': 2000}
#                 }
#             }
#         },
#         'clothes': {
#             'shirts': {
#                 'Nike': {
#                     4001: {'ragac key': 'ragac value'}
#                 }
#             }
#         }
#     },
# {
#         'electronics': {
#             'laptops': {
#                 'apple': {
#                     1001: {'model': 'Macbook Pro', 'price': 6000},
#                     1002: {'model': 'Macbook Air', 'price': 4000}
#                 },
#                 'HP': {
#                     2001: {'model': 'Pavillion', 'price': 2000},
#                     2002: {'model': 'G250', 'price': 2000}
#                 }
#             },
#             'phones': {
#                 'samsung': {
#                     3001: {'model': "S24 Ultra", 'price': 2000}
#                 }
#             }
#         },
#         'clothes': {
#             'shirts': {
#                 'Nike': {
#                     4001: {'ragac key': 'ragac value'}
#                 }
#             }
#         }
#     },
# ]

# print(data)
# print(type(data))
#
# json_string = json.dumps(data)
# print(json_string)
# print(type(json_string))

# with open('test.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)

# from faker import Faker
#
# fake = Faker()
#
# def custom_serialization(obj):
#     if isinstance(obj, Student):
#         return {'name': obj.name, 'age': obj.age, 'courses': obj.courses}
#     raise TypeError("Object Must Be Type Of Student")
#
# class Student:
#     def __init__(self, name, age, courses):
#         self.name = name
#         self.age = age
#         self.courses = courses
#
#     def __str__(self):
#         return self.name
#
# student1 = Student(fake.name_male(), 30, ['Python', 'Java', 'Kotlin', 'C#'])
# student2 = Student(fake.name_female(), 30, ['Python', 'Java', 'Kotlin', 'C#'])
# student3 = Student(fake.name(), 30, ['Python', 'Java', 'Kotlin', 'C#'])
#
# json_list = [student1, student2, student3]

# json_string = json.dumps(json_list, default=custom_serialization, indent=4)
# print(json_string)

# with open('students.json', 'w') as json_file:
#     json.dump(json_list, json_file, default=custom_serialization, indent=4)




###############################################
# Deserialization
###############################################

# json_string = '[{"name": "John", "age": 30, "working": False}, {"name": "John", "age": 30, "working": false}]'
# print(json_string)
# print(type(json_string))

# try:
    # python_data = json.loads(json_string)
    # python_data['age'] = 50
#     print(python_data)
#     print(type(python_data))
# except json.JSONDecodeError as e:
#     print(e)
#     print("JSON Contains Wrong Data Type")
# except Exception as e:
#     print(f"Something Wrong Happened: {e}")


# with open('test.json', 'r') as json_file:
#     python_data = json.load(json_file)
#
# print(f"Deserialized Data: \n{python_data}")
#
# price_of_all_laptops = 0
# for data in python_data:
#     price_of_all_laptops += data['electronics']['laptops']['apple']['1001']['price']
#     print(data['electronics']['laptops']['apple']['1001']['price'])
#
# print(price_of_all_laptops)

# class Student:
#     def __init__(self, name, age, courses):
#         self.name = name
#         self.age = age
#         self.courses = courses
#
# def custom_deserialization(json_obj):
#     return Student(json_obj['name'], json_obj['age'], json_obj['courses'])
#
# with open('students.json', 'r') as json_file:
#     python_data = json.load(json_file, object_hook=custom_deserialization)
#
# print(python_data)
#
# for student in python_data:
#     print(student.name)



# user input - 1. book name, 2. book author, 3. book description, 4. year
# Book - name, author, description, year
# custom_serialization
# write in file


# from faker import Faker
#
# fake = Faker()
#
# print(fake.text())


import json


class Book:
    def __init__(self, name, author, description, year):
        self.name = name
        self.author = author
        self.description = description
        self.year = year

    def to_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "description": self.description,
            "year": self.year
        }

class Student:
    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses

def serialize_book(obj):
    if isinstance(obj, Book):
        return {
            "name": obj.name,
            "author": obj.author,
            "description": obj.description,
            "year": obj.year
        }
    if isinstance(obj, Student):
        return {
            "name": obj.name,
            "age": obj.age,
            "courses": obj.courses
        }

    raise TypeError("Error")

def write_books_to_file(books, filename):
    with open(filename, 'w') as file:
        json.dump(books ,file, indent=4, default=serialize_book)


def get_book_details():
    name = input("Enter book name: ")
    author = input("Enter book author: ")
    description = input("Enter book description: ")
    year = int(input("Enter year of publication: "))
    return Book(name, author, description, year)




# Example usage
# books = []
# num_books = int(input("How many books do you want to add? "))
#
# for _ in range(num_books):
#     books.append(get_book_details())

students = [Student("irakli", "25", ['python']), Student("irakli", "25", ['python']), Student("irakli", "25", ['python'])]
books = [Book('test', 'test', 'test',1999),Book('test', 'test', 'test',1999),Book('test', 'test', 'test',1999)]

whole_list = students + books

write_books_to_file(whole_list, 'books.json')