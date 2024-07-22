#
#
student_list = [
    '1 - Melissa Parker - 91 60 89 84 26',
    '2 - Paige Simon - 39 90 38 74 49',
    '3 - Kevin Atkins - 27 7 89 96 62',
    '4 - Barry Ramos - 94 93 62 30 66',
    '5 - Karen Hudson - 51 15 94 20 8',
    '6 - Jennifer Diaz - 56 31 81 52 50',
    '7 - Robin Smith - 90 3 92 86 14',
    '8 - Kevin Clark - 69 65 47 58 44',
    '9 - Lisa Shields DDS - 92 1 53 40 89',
    '10 - John Kennedy - 21 41 12 15 90',
]

split_dash = []

for data in student_list:
    data = data.split(' - ')
    split_dash.append(data)

# print(split_dash)
final_lst = []

for student in split_dash:
    name = student[1]
    grades = student[2].split()
    print(grades)

    sum_grades = 0
    for grade in grades:
        sum_grades += int(grade)

    avg_grades = sum_grades / len(grades)

    final_lst.append([name, avg_grades])

print(final_lst)



def power(num):
    return num ** 2

number_list = [10, 2, 15, 12, 5, 10, 25, 6]

result = map(power, number_list)
print(list(result))


def calculate_average_grades(student_list):
    result = []
    for student in student_list:
        parts = student.split(" - ")
        name = parts[1].strip()
        grades = list(map(int, parts[2].split()))
        average = sum(grades) / len(grades)
        result.append([name, average])
        return result



strings_list = ['20', '15', '20', '55', '25']
grades = map(int, strings_list)
for grade in grades:
    print(type(grade))