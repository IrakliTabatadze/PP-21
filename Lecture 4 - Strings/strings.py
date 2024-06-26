
# Concatenate
hello = "Hello"
world = "World"
full_string = hello + world
print(full_string)


# Multiply
hello = "Hello"
print(hello * 5)


# Slicing
full_string = "Hello World!!!"
print(full_string[10])
print(full_string[-4])
print(full_string[1:10])
print(full_string[1:])
print(full_string[:10])
print(full_string[::-1])

# Methods
full_string = "Hello World!!!"
check_string = "hello world!!!"

full_string = full_string.lower()
print(full_string.lower() == check_string.lower())
print(full_string.upper())
print(full_string.upper() == check_string.upper())

count_char = full_string.count("u")
print(count_char)

index_char = full_string.index("H")
print(index_char)

print(full_string.startswith("Hello"))
print(full_string.endswith("World!!!"))


# Formatting
name = "John"
last_name = "Doe"
age = 28

full_string = "Hello, I am %s %s" % (name, last_name)
print(full_string)

full_string = "Hello, I am %s, I am %d years old" % (name, age)
print(full_string)

full_string = "Hello I am {}, I am {} years old".format(name, age)
print(full_string)
full_string = "Hello I am {1}, I am {0} years old".format(name, age)
print(full_string)

full_string = f"Hello I am {name}, I am {age} years old"
print(full_string)
full_string = F"Hello I am {name}, I am {age} years old"
print(full_string)


# Encode/Decode
txt = "Hello"
print(txt)
encoded_txt = txt.encode("utf-8")
print(type(encoded_txt))

decoded_txt = encoded_txt.decode()
print(type(decoded_txt))
