
import random

random_number = random.randint(1, 10)
print("Random Number:", random_number)
life = 5

while life > 0:
    print("Life:", life)
    input_number = int(input("Please Enter The Number: "))
    if input_number > random_number:
        print("Number Is Greater")
        life -= 1
    elif input_number < random_number:
        print("Number Is Lower")
        life -= 1
    else:
        print("Congratulation!!! You Win!!!")
        user_input = str(input("Do You Want To Continue?? y/n"))
        if user_input == "y":
            continue
        elif user_input == "n":
            break
else:
    print("You Lose!!! Try Again!!!")