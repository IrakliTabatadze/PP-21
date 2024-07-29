from faker import Faker

fake = Faker()
print(fake.text())



import math

print(math.ceil(2.1))
print(math.floor(2.9))

rad = math.radians(60)
print(math.sin(rad))
print(math.cos(rad))
print(math.tan(rad))

degree = math.degrees(rad)
print(degree)

print(math.fabs(55))
print(math.fabs(-55))

print(math.gcd(19, 10))
print(math.lcm(5, 10))

print(math.factorial(5))

lst = [5, 10, -2, 0, -10, 17, 19, 5.5]
print(math.fsum(lst))

print(math.sqrt(25))

print(math.pow(16, 1/4))

print(math.pi)
print(math.e)


def plus():
    return 10 + 5
def minus():
    return 17-11

func1 = plus()
func2 = minus()
print(func1 + func2)

def plus(num1, num2):
    print(num1)
    print(num2)
    return num1 + num2


res1 = plus(10, 5)
print(res1)
res2 = plus(15, 15)
print(res2)
res3 = plus(11, 13)
print(res3)

response = plus(10, num2=17)
print(response)