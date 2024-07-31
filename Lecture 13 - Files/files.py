#############################################################
# Read File
#############################################################

test_file = open("text_test.txt", "x")

test_file = open('text_test.txt', 'r')
print(test_file.read())
print(test_file.readline())
print(test_file.readline())
read_file = test_file.readlines()

for line in read_file:
    if 'John' in line:
        print(line)

test_file.close()

test_file = open('text_test.txt', 'x') # FileExistsError
test_file = open('text.txt', 'r') # FileNotFoundError

#############################################################
# Write File
#############################################################
lst = ['line 1\n', 'line 2\n', 'line 3\n']

writable_file = open('text_test.txt', '+r')

writable_file.write('Hello From File')
print(writable_file.read())

writable_file.writelines(lst)

print(writable_file.writable(), writable_file.readable())
writable_file.close()


#############################################################
# Append File
#############################################################

writable_file = open('text_test.txt', 'a')

print(writable_file.writable(), writable_file.readable())

writable_file.write("\nNew Line From Append Method")
writable_file.close()


#############################################################
# Context Manager
#############################################################

with open('text_test.txt', '+r') as file:
    read_file = file.readlines()

    with open('writable_file.txt', 'w') as writable_file:
        for line in read_file:
            if "Method" in line:
                writable_file.write(line + '\n')


#############################################################
# OS Module
#############################################################

import os

print(os.listdir())
os.remove('writable_file.txt')
print(os.listdir())
os.mkdir('TestDirectory')
print(os.listdir())
open('TestDirectory/test.txt', 'x')
print(os.listdir())
