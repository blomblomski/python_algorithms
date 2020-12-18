def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        a = 0
        b = 0
        c = 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                lst[c] = left[a]
                a = a + 1
            else:
                lst[c] = right[b]
                b = b + 1
            c = c + 1
        while a < len(left):
            lst[c] = left[a]
            a = a + 1
            c = c + 1
        while b < len(right):
            lst[c] = right[b]
            b = b + 1
            c = c + 1

        return lst


numbers = [44, 16, 83, 7, 67, 21, 45, 10]

print(merge_sort(numbers))
