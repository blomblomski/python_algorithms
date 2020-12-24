from python_algorithms.sorting.bubble_sort import bubble_sort_complete as bs


def intpol_search(lst, x):
    idx0 = 0
    idxn = (len(lst) - 1)
    found = False
    while idx0 <= idxn and x >= lst[idx0] and x <= lst[idxn]:
        # find mid point
        mid = idx0 + int(((float(idxn - idx0) / (lst[idxn] - lst[idx0])) * (x - lst[idx0])))
        # compare the value at mid point with search value
        if lst[mid] == x:
            found = True
            return found
        if lst[mid] < x:
            idx0 = mid + 1
    return found


numbers = [12, 33, 11, 99, 22, 55, 90]

sorted_list = bs.bubble_sort(numbers)

print(intpol_search(sorted_list, 12))
print(intpol_search(sorted_list, 91))
