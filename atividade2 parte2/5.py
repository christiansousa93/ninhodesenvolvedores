# Write a Python program to get the smallest number from a list.

def smallest_num_in_list(list):
    min = list[0]
    for a in list:
        if a < min:
            min = a
    return min


print(smallest_num_in_list([1, 2, -8, 0]))
