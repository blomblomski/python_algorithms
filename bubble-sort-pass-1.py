numbers = [25, 21, 22, 24, 23, 27, 26]

lastElementIndex = len(numbers)-1
print(0, list)
for idx in range(lastElementIndex):
    if numbers[idx] > numbers[idx+1]:
        numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
    print(idx+1, numbers)
