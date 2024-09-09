import json
import pickle
import dill

mylist = ["apple", "banana", "cherry"]
mydict = {"apple": 1, "banana": 2, "cherry": 3}

print(type(mylist), type(mydict))

serialized_list = json.dumps(mylist)
serialized_dict = json.dumps(mydict)

print(type(serialized_list), type(serialized_dict))

deserialized_list = json.loads(serialized_list)
deserialized_dict = json.loads(serialized_dict)

print(type(deserialized_list), type(deserialized_dict))

class Student:
    def __init__(self, name, lastname, year):
        self.name = name
        self.lastname = lastname
        self.year = year

    def __repr__(self):
        return f"Student {self.name}, {self.lastname}, {self.year}"


student1 = Student("John", "Smith", 1997)

def custom_serializer(obj):
    return {
        "name": obj.name,
        "lastname": obj.lastname,
        "year": obj.year
    }

serialized_student = json.dumps(student1)

with open("data.json", "w") as f:
    json.dump(student1, f, default=custom_serializer)

with open("data.json", "r") as f:
    studentdata = json.load(f)

print(studentdata)


pickled_student = pickle.dumps(student1)
print(pickled_student)

with open("data.pckl", "wb") as f:
    pickle.dump(student1, f)

with open("data.pckl", "rb") as f:
    deserialized_student = pickle.load(f)


print(deserialized_student)

sqr = lambda x: x**2

with open("data.pckl", "wb") as f:
    pickle.dump(sqr, f)

with open("data.dill", "wb") as f:
    dill.dump(sqr, f)

with open("data.dill", "rb") as f:
    data = dill.load(f)

print(data(5))


