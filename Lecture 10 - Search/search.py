
###############################################################
# Linear Search
###############################################################
lst = [10, 15, 2, 4, 26, 17, 2]
check_number = 17

def search(lst, x):

    # With ForEach
    for number in lst:
        if number == x:
            return lst.index(number)

    return -1

    # With For Cycle
    for index in range(len(lst)):
        if lst[index] == x:
            return index

    return -1

    # With enumerate Function
    for index, value in enumerate(lst):
        print(f"Index: {index}, Value: {value}")
        if value == x:
            return index

    return -1

search_number = search(lst, check_number)
print(search_number)



###############################################################
# Linear Search Recursively
###############################################################

def search(lst: list, current_index: int, search_item: int):
    if current_index == -1:
        return -1
    if lst[current_index] == search_item:
        return current_index
    return search(lst, current_index - 1, search_item)


lst = [10, 15, 2, 4, 26, 17, 2]
check_number = 2
check_search = search(lst, len(lst) - 1, check_number)
print(check_search)




###############################################################
# Binary Search Iteratively
###############################################################
def binary_search(lst, x):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] < x:
            low = mid + 1
        elif lst[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

numbers_list = [4, 7, 10, 13, 15, 20]
result = binary_search(numbers_list, 12)
print(result)



###############################################################
# Binary Search Recursively
###############################################################
def binary_search(lst, low, high, x):
    if high >= low:
        mid = (low + high) // 2

        if lst[mid] == x:
            return mid

        elif lst[mid] > x:
            return binary_search(lst, low, mid - 1, x)
        else:
            return binary_search(lst, mid + 1, high, x)
    else:
        return -1

numbers_list = [4, 7, 10, 13, 15, 20]
result = binary_search(numbers_list, 0, len(numbers_list) - 1, 5)
print(result)



###############################################################
# Binary Search Nested Lists
###############################################################

import math
nums = [[1, 'hello'], [2, 'hello'], [3, 'hello']]

def binerySearch(n: list, t: int):
    low = 0
    high = len(n) - 1
    while low <= high:
        middleindex = math.floor((low + high) / 2)
        if t in n[middleindex]:
            return middleindex
        elif t > n[middleindex][0]:
            low = middleindex + 1
        else:
            high = middleindex - 1
    return -1