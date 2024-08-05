departments = {
    "HR": [
        {"first_name": "Alice", "last_name": "Johnson", "age": 30, "salary": 60000},
        {"first_name": "Bob", "last_name": "Smith", "age": 45, "salary": 75000}
    ],
    "IT": [
        {"first_name": "Carol", "last_name": "Taylor", "age": 25, "salary": 90000},
        {"first_name": "David", "last_name": "Brown", "age": 35, "salary": 85000},
    ],
    "Sales": [
        {"first_name": "Eve", "last_name": "Davis", "age": 28, "salary": 55000},
        {"first_name": "Frank", "last_name": "Miller", "age": 50, "salary": 70000}
    ]
}


def calculate_avarage_salary(departments):
    average_salaries = {}
    for department, employees in departments.items():
        total_salary = sum(employee['salary'] for employee in employees)
        average_salary = total_salary / len(employees)
        average_salaries[department] = average_salary

    return average_salaries

print(calculate_avarage_salary(departments))





company = {
    "HR": [
        {"name": "John", "surname": "Doe", "age": 35, "salary": 50000},
        {"name": "Jane", "surname": "Smith", "age": 28, "salary": 45000}
    ],
    "IT": [
        {"name": "Mike", "surname": "Johnson", "age": 40, "salary": 75000},
        {"name": "Sarah", "surname": "Williams", "age": 32, "salary": 70000},
        {"name": "Tom", "surname": "Brown", "age": 27, "salary": 60000}
    ],
    "Finance": [
        {"name": "Emily", "surname": "Davis", "age": 45, "salary": 80000},
        {"name": "David", "surname": "Wilson", "age": 38, "salary": 72000}
    ]
}

for department in company:
    total_salary = 0
    average_salary = 0
    for employee in company[department]:
        total_salary += employee["salary"]
        average_salary = total_salary / len(company[department])

    print(f"{department} average salary: {average_salary}")


def plus(num1, num2):
    return num1 + num2

def substruction(num1, num2):
    return num1 - num2

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y
}

num1 = int(input("Please input the number: "))
num2 = int(input("Please input the number: "))
operator = str(input("Please input the operator: "))

print(operations[operator](num1, num2))