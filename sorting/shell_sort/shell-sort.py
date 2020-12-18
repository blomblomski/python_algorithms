def shell_sort(lst):
    distance = len(lst) // 2
    while distance > 0:
        for i in range(distance, len(lst)):
            temp = lst[i]
            j = i

            # sort the sub list for distance
            while j >= distance and lst[j - distance] > temp:
                lst[j] = lst[j - distance]
                j = j - distance
            lst[j] = temp
        distance = distance // 2

    return lst


numbers = [26, 17, 20, 11, 23, 21, 13, 18, 24, 14, 12, 22, 16, 15, 19, 25]
print(shell_sort(numbers))

