from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb://localhost:27017/')

client = MongoClient('localhost', 27017)

db = client.mongo_db

students = db.students


students.insert_one({'first_name': 'Anna', 'courses': ['Python', 'SQL', 'MongoDB']})

student_id = students.insert_one({'first_name': 'Bob', 'last_name': 'Smith', 'age': 22}).inserted_id
print(f"id:  {student_id}")


student1 = {'first_name': 'Sam', 'last_name': 'Smith', 'courses': ['Math', 'English'], 'age': 23}
student2 = {'first_name': 'Sean', 'last_name': 'Johnson', 'courses': ['Algorithm', 'English'], 'age': 24}
student3 = {'first_name': 'Kate', 'last_name': 'Anderson', 'courses': ['Algorithm', 'English'], 'age': 25}

students_lst = [student1, student2, student3]
#
students.insert_many(students_lst)



for student in students.find():
    print(student)

for smith in students.find({'first_name': 'Sam', 'last_name': 'Smith'}):
    print(smith)


# 67168db48d08e94d1ebea33e

for student in students.find({'_id': ObjectId('67168db48d08e94d1ebea33e')}):
    print(student)


for student in students.find({'courses': {"$exists": True}}):
    print(student)


for student in students.find({'courses': {"$in": ['Python', 'English']}}):
    print(student)


for student in students.find({'age': {'$lte': 24}}):
    print(student)


students.update_one({'_id': ObjectId('671691a69b45d8f1daf2ad84')}, {'$set': {'courses': ['Python', 'MongoDB', 'JAVA']}})

students.update_many({'last_name': 'Smith'}, {'$set': {'courses': ['Python', 'MongoDB', 'JAVA']}})

students.delete_one({'_id': ObjectId('671685ba7bc93d683e70ca6c')})

students.delete_many({'age': {'$gt': 22}})