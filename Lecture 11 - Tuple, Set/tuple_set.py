#############################################################
# Tuple
#############################################################

empty_tuple = ()
empty_tuple2 = tuple()

print(type(empty_tuple))
print(type(empty_tuple2))


one_element_tuple = ("hello",)
print(type(one_element_tuple))


multiple_el_tuple = (10, .5, True, "Hello", [10, 11, 12])
multiple_el_tuple[-1].append(15)
print(multiple_el_tuple)


tuple1 = (1, 2, 3, 3, 3, 2)
tuple2 = (4, 5, 6)

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

lst1.extend(lst2)
print(lst1)

print(tuple1 + tuple2)
print(tuple1 * 5)
print(tuple1)
print(tuple2)


tuple1 = (1, 2, 3, 3, 3, 2)
print(tuple1.index(2))
print(tuple1.count(2))


def func(*args):
    print(args)

    last_element = args[-1]
    last_element += 10
    print(last_element)
    print(args)

func("Hello", "hi", 1, 2, 3)


lst = ["Hello", "hi", 1, 2, 3]

for index, value in enumerate(lst):
    print(index, value)


tuple1 = ("Hello", "hi", 1, 2, 3)
el1, el2, *other_elements = tuple1
print(el1, el2, other_elements)


#############################################################
# Set
#############################################################

empty_set = set()
print(empty_set)

full_set = {1, "hello", 2, 10, 3, 4, 5}
for el in full_set:
    print(el)

print(full_set)

full_set.add("hi")
print(full_set)

full_set2 = full_set.copy()
full_set.add("Irakli")
print(full_set2)
print(full_set)

full_set.remove(10)
print(full_set)
print(full_set.pop())
print(full_set)
print(full_set.pop())
print(full_set)


filled_set1 = {True, 1, 2, 3, 4, 5, False, 0}
print(filled_set1)
filled_set2 = {3, 4, 5, 6, 7}

print(filled_set1.difference(filled_set2))
filled_set1.difference_update(filled_set2)
print(filled_set1)

print(filled_set1.intersection(filled_set2))
filled_set1.intersection_update(filled_set2)
print(filled_set1)

union_set = filled_set1.union(filled_set2)

print(union_set)


#############################################################
# FrozenSet
#############################################################

filled_set1 = {True, 1, 2, 3, 4, 5, False, 0, 10, 20, 30}
frozen_set = frozenset(filled_set1)
print(filled_set1)
print(frozen_set)

print(frozen_set.union(filled_set1))



#############################################################
# Task
#############################################################

def unique_numbers(numbers):
    return list(set(numbers))


numbers = (1, 2, 3, 4, 'hello', 2, 5, 7, 'hello', 7, 2, 2, 4)
print(unique_numbers(numbers))