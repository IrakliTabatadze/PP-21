###############################################
# lambda
###############################################


def add(x, y):
    return x + y


add_lambda = lambda x, y: x + y

print(add)
print(add_lambda)

add_lambda = (lambda x=10, y=15: x + y)
print(add_lambda(25))


lst = [lambda arg=x: arg*10 for x in range(1, 11)]
# print(lst)
for func in lst:
    print(func())


lst = [(lambda arg=x: arg*10)() for x in range(1, 11)]
print(lst)


lst = [5, 10, 2, 3, 17, 25, 55]
even_list = [(lambda x=num: x if x%2==0 else "Odd")() for num in lst]
print(even_list)



###############################################
# partial
###############################################

from functools import partial

def mult(x, y):
    return x * y

multiplication = partial(mult, x=5)
print(multiplication(y=10))
print(multiplication(y=20))
print(multiplication(y=30))
print(multiplication(y=40))
print(multiplication(x=10, y=40))



###############################################
# reduce
###############################################

from functools import reduce

lst = [10, 15, 20]

sum_of_list = reduce(lambda a, b: a + b, lst)
print(sum_of_list)


fact = reduce(lambda a, b: a * b, range(1, 6))
print(fact)


###############################################
# map
###############################################

numbers_list = [10, 2, 15, 3, 15]

def mult(x):
    return x * 5

result = list(map(mult, numbers_list))

print(result)


powers = list(map(lambda x: [x ** 2, x ** 3], numbers_list))
print(powers)





###############################################
# filter
###############################################
numbers_list = [10, 2, 15, 3, 15]

odd_numbers = filter(lambda x: x%2==1, numbers_list)
print(list(odd_numbers))



###############################################
# zip
###############################################
keywords = ['first name', 'last name', 'age']
values = ['John', 'Doe', 25]

data = zip(keywords, values)
print(list(data))
