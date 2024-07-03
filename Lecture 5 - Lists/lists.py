##################################################################
# Convert Char To ASCII/Unicode Numbers
##################################################################
ascii_char = ord("ა")
print(ascii_char)



##################################################################
# Regular Expression (ReGex)
##################################################################

import re

text = "Python is the best programming language bat"

pattern = r"[aeiou]"
matches = re.findall(pattern, text)

pattern = r'b..t'
matches = re.findall(pattern, text)

pattern = r'b.*t'
matches = re.match(pattern, text)

print(matches)



##################################################################
# Lists
##################################################################

empty_list = []
empty_list2 = list()

print(empty_list2)
print(empty_list)


hobbies = ["Programming", "Music", "Walking", "Talking"]

print(hobbies)

print(hobbies[-1])
print(hobbies[0:2])
print(hobbies[1:])
print(hobbies[:3])
print(hobbies[::-1])


##################################################################
# List Methods
##################################################################

list_1 = ["Programming", "Music", "Walking", "Talking", 3, 1, 2, 3, 4, True, 2.5]
list_2 = list_1.copy()

list_1.clear()

print(list_1)
print(list_2)
print(id(list_1))
print(id(list_2))

list_1.append("Apended Element")
print(list_1)
print(list_1.index("Walking"))

list_1.insert(2, "Inserted Information")
print(list_1)
print(list_1.index("Walking"))


count_three = list_1.count(3)
print(count_three)

for i in range(count_three):
    list_1.remove(3)
print(list_1)

popped_item = list_1.pop(2)
print(popped_item)
print(list_1)


list_1.reverse()
print(list_1)

integer_list = [5, 10, 1, 3, 2, 15, 26, 11, 5.5]

integer_list.sort(reverse=True)
print(integer_list)


hobbies = ["Programming", "Music", "Walking", "Talking"]
hobbies.sort()
print(hobbies)


integer_list = [i for i in range(0, 10, 2)]
print(f"First List: {integer_list}")

integer_list2 = []
for i in range(10):
    integer_list2.append(i)

print(f"Second List: {integer_list2}")

list1 = [5, 10, 7, 2, 9, 6, 8]

even_list = [i for i in list1 if i % 2 == 0]
print(even_list)

even_list_2 = []
for i in list1:
    if i % 2 == 0:
        even_list_2.append(i)
print(even_list_2)





##################################################################
# Matrix
##################################################################


matrix = [
    [1, 2, 3],
    [5, 6, 7],
    [8, 9, 10]
]

index_one = matrix[1]
print(matrix[1][2])

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        print(matrix[row][column])


for row in matrix:
    print(row)
    for column in row:
        print(column)




