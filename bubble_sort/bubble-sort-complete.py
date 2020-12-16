def bubble_sort(lst):
    lastElementIndex = len(lst) - 1
    for passNo in range(lastElementIndex, 0, -1):
        for idx in range(passNo):
            if lst[idx] > lst[idx + 1]:
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
    return lst


print(bubble_sort([25, 21, 22, 24, 23, 27, 26]))
