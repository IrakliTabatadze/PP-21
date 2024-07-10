
def plus(num1, num2, num3, num4=None, num5=None):
    print(f"Num1: {num1}, Num2: {num2}, Num3: {num3}, Num4: {num4}, Num5: {num5}")
    return num1 + num2


plus(10, 20, num4=10, num3=15, num5=25)


def test(name, last_name, *args, **kwargs):
    print(args)
    print(kwargs)
    return 0

test(10, 15, "Hello", "Hi", .9, False, name1='John')


def plus(num1, num2, num3, *args):
    print(num1, num2, num3, args)
    return num1 + num2 + num3

lst = [15, 11, 12, 10, 10, 15, 12]
sum_num = plus(*lst)


x = 10

def legb():
    x = 5
    x = x + 10
    print(x)
    def test2():
        global x
        x += 10
        print(x)
    test2()

legb()




import math
def circle_area(pi):
    def whole_area(radius):
        return pi * radius ** 2

    return whole_area

del circle_area
area = circle_area(math.pi)
whole = area(10)
print(area)


def rec_func(x):
    def nester_func():
        return "Nested Func"
    if x == 0:
        return nester_func()
    return rec_func(x-1)

func = rec_func(10)
print(func)





def checker(row, char):
    row = row.upper()
    char = char.upper()

    count_char = row.count(char)

    count = 0
    for ch in row:
        if ch == char:
            count += 1

    return count, count_char

count = checker("Hello World", "o")
print(count)