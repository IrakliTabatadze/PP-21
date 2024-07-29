
try:
    num1 = int(input("Enter the number: "))
    num2 = int(input("Enter the number: "))

    print(num1 / num2)

except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Final Block")

print("After Try Except")




lst = [5, 1, 3, 2, 10, 5, 8]
lst = [["John", 25], ["Anna", 21], ['Kate', 22]]
lst.sort(key=lambda a: a[1])
print(lst)



def bubble_sort(lst: list) -> list:

    length = len(lst)

    for i in range(length):
        swapped = False

        for j in range(length - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        if swapped == False:
            break


lst = [5, 1, 3, 2, 10, 5, 8]
bubble_sort(lst)
print(lst)



def selection_sort(lst):

    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]

lst = [5, 1, 3, 2, 10, 5, 8]
selection_sort(lst)
print(lst)




def quick_sort(lst: list):
    length = len(lst)

    if length <= 1:
        return lst
    else:
        pivot = lst.pop()

    greater_numbers = []
    lower_numbers = []

    for number in lst:
        if number > pivot:
            greater_numbers.append(number)
        else:
            lower_numbers.append(number)

    return quick_sort(lower_numbers) + [pivot] + quick_sort(greater_numbers)

lst = [5, 1, 3, 2, 2, 2, 10, 10, 10, 5, 8]
sorted_list = quick_sort(lst)
print(sorted_list)