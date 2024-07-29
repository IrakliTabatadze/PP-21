

def flatten_tuple(tupl):
    flat_list = []

    def flatten(tupl):
        for element in tupl:
            if isinstance(element, tuple):
                print(f"Tuple: {element}")
                flatten(element)
            else:
                print(f"Integer: {element}")
                flat_list.append(element)

    flatten(tupl)

    return tuple(flat_list)



input_tuple = (1, (2, 3), (4, (5, 6)))
flat_tuple = flatten_tuple(input_tuple)
print(flat_tuple)




def irl(irlTuple):
    result = []
    for items in irlTuple:
        if isinstance(items, tuple):
            result.extend(irl(items))
        else:
            result.append(items)
    return tuple(result)


input_tuple = (1, (2, 3), (4, (5, 6)))
flat_tuple = irl(input_tuple)
print(flat_tuple)






def swap_elements(tuple_for_swap):
    swapped_tuple = (tuple_for_swap[-1],) + tuple_for_swap[1:-1] + (tuple_for_swap[0],)

    return swapped_tuple

input_tuple = (1, 2, 3, 5, 2, 10, 4)
swapped = swap_elements(input_tuple)
print(swapped)





def swap_element(tuple_swap):

    first, *middle, last = tuple_swap

    return (last, *middle, first)

input_tuple = (1, 2, 3, 5, 2, 10, 4)
swapped = swap_element(input_tuple)
print(swapped)