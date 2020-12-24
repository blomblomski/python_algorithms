def linear_search(lst, item):
    index = 0
    found = False
    # Match the value with each data element
    while index < len(lst) and found is False:
        if lst[index] == item:
            found = True
        else:
            index = index + 1

    return found


numbers = [12, 33, 11, 99, 22, 55, 90]
print(linear_search(numbers, 12))
print(linear_search(numbers, 91))
