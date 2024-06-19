#
# number1 = 10
# Increment
# number1 += 1
# print(number1)
#
#
# and_statement = True and True
# print(and_statement)
#
# or_statement = False or False
# print(or_statement)
#
# not_statement = not (True and False or False)
# print(not_statement)

number1 = 10
number2 = 10

is_or_not = number1 is number2
print(is_or_not)
is_or_not = number1 is not number2
print(is_or_not)


string_object = 'Hello World!!!'
print('h' not in string_object)

#######################################################
number1 = 10
number2 = 20

print("number1 > number2:", number1 > number2)
print("number1 < number2:", number1 < number2)
print("number1 >= number2:", number1 >= number2)
print("number1 <= number2:", number1 <= number2)
print("number1 == number2:", number1 == number2)
print("number1 != number2:", number1 != number2)

##########################################################
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 < number2:
    print("If Block Worked")
elif number1 == number2:
    print("Elif Block Worked")
elif number1 > number2:
    print("Second Elif Block Worked")

print("If Else Finished")

###########################################################
number = int(input("Enter a number: "))
sum_of_number = 0

if number > 0:
    sum_of_number += number
    number = int(input("Enter a number: "))
    if number > 0:
        sum_of_number += number
        number = int(input("Enter a number: "))
        if number > 0:
            sum_of_number += number
            print("Sum Of Number = ", sum_of_number)
        else:
            print("Third Number Is Less Or Equal To Zero")
    else:
        print("Second Number is Less Or Equal To Zero")
else:
    print("First Number Is Less Or Equal To Zero")


########################################################################
number = int(input("Enter a number: "))

result = "Zero" if number == 0 else "Greater Than Zero"
print(result)
