def binarySearch(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (high + low) // 2
        guess = arr[middle]
        if guess == item:
            return middle
        if guess > item:
            high = middle - 1
        else:
            low = middle + 1
    return None

myArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binarySearch(myArr, 2))