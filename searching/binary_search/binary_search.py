from python_algorithms.sorting.bubble_sort import bubble_sort_complete as bs


def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if lst[midpoint] == item:
            found = True
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


numbers = [12, 33, 11, 99, 22, 55, 90]
sorted_list = bs.bubble_sort(numbers)

print(binary_search(sorted_list, 12))
print(binary_search(sorted_list, 91))
