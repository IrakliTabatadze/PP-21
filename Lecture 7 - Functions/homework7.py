
def sum_of_digits(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_of_digits(number // 10)

print(sum_of_digits(123))



def fibonacci(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


def reverse_str(sentence):
    if not sentence:
        return ""
    return sentence[-1] + reverse_str(sentence[:-1])

print(reverse_str("Hello"))



word = "Hello"
reverse_word = ""

for i in range(len(word)-1, -1, -1):
    reverse_word += word[i]

print(word)
print(reverse_word)
