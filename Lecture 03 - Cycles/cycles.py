
txt = "Hello World!"
iterator_txt = iter(txt)

print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))






number = 0

while number < 10:
    number += 1
    if number == 3:
        continue
    print(number)

else:
    print("Cycle Finished Successfully")


while True:
    number = int(input("Enter a number: "))
    print(number)
    if number <= 0:
        print("Number Is Zero Or Negative")
        break


count = 5

while count > 0:
    number = int(input('Enter a number: '))
    if number <= 0:
        count -= 1
else:
    print("You Entered a negative number five times")



for i in range(10, 5, -3):
    print(i)


txt = "Hello World!"

for letter in txt:
    print(letter)


for i in range(1, 11):
    for j in range(1, 11):
        print("i =", i, "j =", j)



for i in range(1, 11):
    print(i, end=' ')
    if i == 5:
        print()


print("irakli","tabatadze", "IT", "Step", "Academy", sep="@")



import random
# from random import randint

random_number = random.random()
random_number = random.randint(5, 10)
random_number = random.randrange(5, 10)
print(random_number)