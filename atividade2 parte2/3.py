# Write a Python program to multiplies all the items in a list.

def multiply_list(items):
    tot = items[0]
    for x in items:
        tot *= x
    return tot


print(multiply_list([1, 2, -8]))
